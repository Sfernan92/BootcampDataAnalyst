#!/usr/bin/env python3
"""Arrabal / Somos F5 · laboratorio GoalZone.

Ejecuta análisis completo en la nube desde GitHub Actions. Datos externos
obtenidos de una copia pública del caso docente GoalZone, no datos operativos
verificados de una compañía. Python 3.11+.

Uso: python lab/analisis.py
Prueba offline: python lab/analisis.py --input /ruta/fitness_class_2212.csv
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import textwrap
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Solo gráficos PNG; Plotly genera la parte interactiva.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from scipy.stats import chi2_contingency, pointbiserialr

REPO = Path(__file__).resolve().parents[1]
DATASET_URL = "https://raw.githubusercontent.com/xrander/fitness_class_project/master/fitness_class_2212.csv"
DATASET_FALLBACK = "https://raw.githubusercontent.com/MarcoABarrera/Fitness_class_dataset/main/fitness_class_2212.csv"
ORANGE = "#FF9500"
PURPLE = "#3C26F1"
BLACK = "#191919"
TENURE_BINS = [-np.inf, 3, 6, 12, 24, np.inf]
TENURE_LABELS = ["0–3", "4–6", "7–12", "13–24", "25+"]
FEATURES = {
    "months_as_member": "Antigüedad del socio",
    "days_before_num": "Antelación de reserva",
    "category": "Categoría de clase",
    "time": "Horario",
    "day_of_week_normalized": "Día de la semana",
}
NEEDED = {"booking_id", "months_as_member", "days_before", "category", "time", "day_of_week", "attended"}


def download_csv(path: Path, urls: tuple[str, ...] = (DATASET_URL, DATASET_FALLBACK)) -> str:
    """Descarga CSV y verifica esquema; NUNCA reemplaza por datos sintéticos."""
    errors = []
    path.parent.mkdir(parents=True, exist_ok=True)
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 ArrabalKPILab/1.0"})
            with urllib.request.urlopen(req, timeout=35) as response:
                contents = response.read()
            if len(contents) < 1000 or contents[:100].lstrip().lower().startswith((b"<html", b"<!doctype")):
                raise ValueError("No se ha recibido un CSV válido")
            from io import BytesIO
            header = pd.read_csv(BytesIO(contents), nrows=0).columns.tolist()
            if not NEEDED.issubset(header):
                raise ValueError(f"Esquema incompatible: {sorted(NEEDED - set(header))}")
            tmp = path.with_suffix(".partial")
            tmp.write_bytes(contents)
            tmp.replace(path)
            return url
        except (ValueError, OSError, urllib.error.URLError, pd.errors.ParserError) as err:
            errors.append(f"{url}: {err}")
    raise RuntimeError("No se pudo descargar el CSV original:\n" + "\n".join(errors))


def clean_goalzone(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    missing = NEEDED - set(raw.columns)
    if missing:
        raise ValueError(f"Esquema GoalZone incompleto: {sorted(missing)}")
    d = raw.copy()
    d["booking_id"] = d["booking_id"].astype("string").str.strip()
    duplicates = int(d["booking_id"].duplicated().sum())
    if duplicates:
        raise ValueError(f"booking_id duplicado: {duplicates} (se requiere 1 fila por reserva)")
    d["attended"] = pd.to_numeric(d["attended"], errors="coerce")
    bad_target = ~d["attended"].isin([0, 1])
    d.loc[bad_target, "attended"] = np.nan
    d["months_as_member"] = pd.to_numeric(d["months_as_member"], errors="coerce")
    d["days_before_num"] = pd.to_numeric(
        d["days_before"].astype("string").str.extract(r"(\d+(?:\.\d+)?)", expand=False), errors="coerce"
    )
    d["category"] = d["category"].astype("string").str.strip().replace({"-": pd.NA, "": pd.NA})
    d["time"] = d["time"].astype("string").str.upper().str.strip().replace({"": pd.NA})
    weekdays = {"mon": "Lunes", "tue": "Martes", "wed": "Miércoles", "thu": "Jueves", "fri": "Viernes", "sat": "Sábado", "sun": "Domingo"}
    d["day_of_week_normalized"] = d["day_of_week"].astype("string").str.strip().str.lower().str[:3].map(weekdays)
    d["tenure_group"] = pd.cut(d["months_as_member"], TENURE_BINS, labels=TENURE_LABELS)
    quality = {
        "filas_origen": len(raw),
        "reservas_con_target_valido": int(d["attended"].notna().sum()),
        "reservas_sin_target_valido": int(bad_target.sum()),
        "ids_duplicados": duplicates,
        "nulos_antiguedad": int(d["months_as_member"].isna().sum()),
        "nulos_anticipacion": int(d["days_before_num"].isna().sum()),
        "nulos_categoria": int(d["category"].isna().sum()),
        "nulos_dia_normalizado": int(d["day_of_week_normalized"].isna().sum()),
    }
    return d, quality


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if total <= 0:
        return (math.nan, math.nan)
    p = successes / total
    zz = z * z
    denominator = 1 + zz / total
    centre = (p + zz / (2 * total)) / denominator
    margin = z * math.sqrt(p * (1 - p) / total + zz / (4 * total * total)) / denominator
    return max(0, centre - margin), min(1, centre + margin)


def segment_rates(df: pd.DataFrame, group: str) -> pd.DataFrame:
    d = df.dropna(subset=["attended", group])
    out = d.groupby(group, observed=True).agg(
        reservas=("attended", "size"), asistencias=("attended", "sum")
    ).reset_index().rename(columns={group: "segmento"})
    out["asistencias"] = out["asistencias"].astype(int)
    out["tasa_asistencia"] = out["asistencias"] / out["reservas"]
    intervals = [wilson_interval(int(s), int(n)) for s, n in zip(out["asistencias"], out["reservas"])]
    out["ic95_inf"] = [v[0] for v in intervals]
    out["ic95_sup"] = [v[1] for v in intervals]
    out["segmento"] = out["segmento"].astype(str)
    return out


def metric_association(df: pd.DataFrame, feature: str) -> dict:
    x = df[feature]
    numeric = feature in ("months_as_member", "days_before_num")
    if numeric:
        pair = pd.DataFrame({"x": pd.to_numeric(x, errors="coerce"), "y": df["attended"]}).replace([np.inf, -np.inf], np.nan).dropna()
        method = "r punto-biserial"
    else:
        pair = pd.DataFrame({"x": x.astype("string"), "y": df["attended"]}).dropna()
        method = "V de Cramér (sin signo)"
    base = {"metrica": feature, "nombre": FEATURES[feature], "metodo": method, "n": len(pair), "coeficiente": np.nan, "p_value": np.nan}
    if len(pair) < 20 or pair["x"].nunique() < 2 or pair["y"].nunique() < 2:
        return base
    if numeric:
        r, p = pointbiserialr(pair["y"], pair["x"])
        base.update(coeficiente=float(r), p_value=float(p))
    else:
        contingency = pd.crosstab(pair["x"], pair["y"])
        chi2, p, _, _ = chi2_contingency(contingency, correction=False)
        v = math.sqrt((chi2 / len(pair)) / (min(contingency.shape) - 1))
        base.update(coeficiente=float(v), p_value=float(p))
    return base


def adjust_bh(pvalues: pd.Series) -> pd.Series:
    ps = pd.to_numeric(pvalues, errors="coerce")
    valid = ps.dropna().sort_values()
    q = pd.Series(np.nan, index=ps.index, dtype=float)
    if len(valid):
        ranked = valid * len(valid) / np.arange(1, len(valid) + 1)
        q.loc[valid.index] = ranked[::-1].cummin()[::-1].clip(upper=1)
    return q


def compute_metrics(d: pd.DataFrame) -> tuple[dict, pd.DataFrame]:
    eligible = d["attended"].notna()
    n = int(eligible.sum())
    attended = int(d.loc[eligible, "attended"].sum())
    lo, hi = wilson_interval(attended, n)
    kpi = {"reservas_elegibles": n, "asistencias_confirmadas": attended,
           "tasa_asistencia": attended / n if n else None, "tasa_ic95_inf": lo, "tasa_ic95_sup": hi,
           "relacion_estructural": "asistencias = reservas_elegibles × tasa_asistencia",
           "unidad": "reserva", "limitacion": "Proxy, no mide satisfacción ni usuarios recurrentes"}
    corr = pd.DataFrame([metric_association(d, f) for f in FEATURES])
    corr["q_value_bh"] = adjust_bh(corr["p_value"])
    corr["significativo_fdr_5pct"] = corr["q_value_bh"].lt(0.05).fillna(False)
    return kpi, corr


def plot_tree(corr: pd.DataFrame, dest: Path) -> None:
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    fig.patch.set_facecolor("#FFFFFF")
    ax.text(.5, .96, "GoalZone · árbol de métricas y asociaciones", ha="center", fontsize=20, weight="bold", color=BLACK)
    ax.text(.50, .79, "TASA DE ASISTENCIA · proxy por reserva", ha="center", fontsize=14,
            color="white", weight="bold", bbox=dict(boxstyle="round,pad=.8", fc=PURPLE, ec="none"))
    positions = np.linspace(.105, .895, len(FEATURES))
    for idx, (feature, name) in enumerate(FEATURES.items()):
        row = corr[corr["metrica"] == feature].iloc[0]
        coef = row["coeficiente"]
        short = "r" if "biserial" in row["metodo"] else "V"
        coef_label = "No estimable" if pd.isna(coef) else f"{short} = {coef:+.3f}" if short == "r" else f"V = {coef:.3f}"
        q = row["q_value_bh"]
        q_label = f"q = {q:.3g}" if pd.notna(q) else "q = n/d"
        x = positions[idx]
        ax.annotate("", xy=(x, .46), xytext=(.5, .73), arrowprops=dict(arrowstyle="->", lw=1.4, ls="--", color="#999999"))
        ax.text(x, .39, f"{textwrap.fill(name, width=17)}\n{coef_label}\n{q_label}",
                fontsize=10, ha="center", va="center", color=BLACK,
                bbox=dict(boxstyle="round,pad=.7", fc="#FFF5D6", ec=ORANGE, lw=1.1))
    ax.text(.5, .13, "Identidad de volumen: asistencias = reservas elegibles × tasa de asistencia", ha="center", fontsize=12, color=PURPLE, weight="bold")
    ax.text(.5, .05, "Flechas discontinuas = hipótesis exploratorias, NO causalidad.\n"
            "r y V de Cramér son métodos diferentes; no comparar su tamaño directamente.",
            ha="center", fontsize=10, color="#555555")
    fig.savefig(dest, dpi=155, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_interactive_figure(d: pd.DataFrame) -> go.Figure:
    categories = ["Todas"] + sorted(d["category"].dropna().unique().tolist())
    fig = go.Figure()
    for i, category in enumerate(categories):
        subset = d if i == 0 else d[d["category"] == category]
        rate = segment_rates(subset, "tenure_group")
        # Conservar todos los tramos y representar 0 registros como NaN.
        rate = rate.set_index("segmento").reindex(TENURE_LABELS).reset_index()
        percentages = rate["tasa_asistencia"] * 100
        fig.add_trace(go.Bar(
            x=rate["segmento"], y=percentages, name=category, visible=(i == 0),
            marker_color=PURPLE if i == 0 else ORANGE,
            customdata=np.column_stack([rate["reservas"].fillna(0), rate["asistencias"].fillna(0)]),
            error_y={"type": "data", "array": ((rate["ic95_sup"] - rate["tasa_asistencia"]) * 100).fillna(0).tolist(),
                     "arrayminus": ((rate["tasa_asistencia"] - rate["ic95_inf"]) * 100).fillna(0).tolist(), "visible": True},
            hovertemplate="Antigüedad: %{x} meses<br>Asistencia: %{y:.1f}%<br>Reservas: %{customdata[0]:.0f}<br>Asistencias: %{customdata[1]:.0f}<extra></extra>",
        ))
    buttons = []
    for idx, category in enumerate(categories):
        visibility = [j == idx for j in range(len(categories))]
        buttons.append(dict(label=category, method="update", args=[{"visible": visibility}, {"title": f"Asistencia por antigüedad · {category}"}]))
    fig.update_layout(
        title="Asistencia por antigüedad · Todas", title_x=.5,
        xaxis_title="Antigüedad del socio (meses)", yaxis_title="Tasa de asistencia (%)",
        yaxis={"range": [0, 105]}, height=530,
        margin=dict(l=52, r=25, t=110, b=65), showlegend=False,
        paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
        updatemenus=[dict(type="dropdown", x=.01, y=1.24, xanchor="left", yanchor="top", buttons=buttons,
                         bgcolor="#FFF5D6", bordercolor=ORANGE, showactive=True)],
        annotations=[dict(text="Filtrar categoría:", x=.01, y=1.30, xref="paper", yref="paper", showarrow=False, xanchor="left")],
        font={"family": "Arial, sans-serif", "color": BLACK},
    )
    return fig


def create_report(d: pd.DataFrame, kpi: dict, corr: pd.DataFrame, quality: dict, source: str) -> str:
    n, a = kpi["reservas_elegibles"], kpi["asistencias_confirmadas"]
    lines = [
        "# Informe de laboratorio · GoalZone", "",
        "> **Datos docentes públicos**, no evidencia auditada de operaciones reales de una empresa.", "",
        f"**Fuente CSV:** {source}", "",
        "## KPI observable", "",
        f"- Reservas elegibles: **{n:,}**", f"- Asistencias confirmadas: **{a:,}**",
        f"- Tasa de asistencia: **{kpi['tasa_asistencia']:.1%}**" if n else "- Tasa: no estimable",
        f"- IC Wilson del 95 %: **[{kpi['tasa_ic95_inf']:.1%}; {kpi['tasa_ic95_sup']:.1%}]**" if n else "- IC: no estimable",
        "", "**Identidad aritmética:** asistencias = reservas elegibles × tasa de asistencia.",
        "Esta identidad no es evidencia causal de una palanca.", "", "## Calidad del dato", "",
    ]
    lines += [f"- {key.replace('_', ' ')}: {value}" for key, value in quality.items()]
    lines += ["", "## Asociaciones con `attended`", "",
              "| Variable | Método | Coeficiente | n | q BH |", "|---|---|---:|---:|---:|"]
    for _, row in corr.iterrows():
        fmt = lambda x: f"{x:.4g}" if pd.notna(x) else "n/d"
        lines.append(f"| {row['nombre']} | {row['metodo']} | {fmt(row['coeficiente'])} | {row['n']} | {fmt(row['q_value_bh'])} |")
    lines += [
        "", "**Lectura:** q de Benjamini–Hochberg < 0,05 indica una asociación exploratoria significativa, no causalidad.",
        "El coeficiente r punto-biserial tiene signo; V de Cramér carece de signo y no es comparable directamente con r.",
        "", "## Limitaciones", "",
        "- Grano del dataset: **reserva**, no socio. No hay un ID de persona que permita medir recurrencia.",
        "- La asistencia no demuestra que la clase haya sido satisfactoria.",
        "- La antigüedad puede mostrar sesgo de supervivencia: quienes persisten podrían ser quienes ya participaban más.",
        "- Las asociaciones bivariadas no controlan confusores ni prueban que cambiar un input cambie la North Star.",
        "- Faltan fechas individuales completas para obtener una North Star semanal real.",
        "", "## Pregunta de discusión", "",
        "> Si la antigüedad muestra asociación con la asistencia, ¿es una palanca sobre la que producto pueda actuar hoy?",
        "", "Propuesta contrastable: experimentar con mejoras de onboarding y medir asistencia temprana y retención posterior.", "",
    ]
    return "\n".join(lines)


def html_report(kpi: dict, corr: pd.DataFrame, quality: dict, interactive: go.Figure, source: str) -> str:
    plot_html = pio.to_html(interactive, full_html=False, include_plotlyjs=True, config={"displaylogo": False, "responsive": True})
    rows = "".join(
        f"<tr><td>{escape(str(r.nombre))}</td><td>{escape(str(r.metodo))}</td>"
        f"<td>{r.coeficiente:.3f}</td><td>{r.n}</td><td>{r.q_value_bh:.3g}</td></tr>"
        for r in corr.itertuples() if pd.notna(r.coeficiente) and pd.notna(r.q_value_bh)
    )
    rate = kpi['tasa_asistencia']
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arrabal · Laboratorio GoalZone</title><style>
:root{{--orange:{ORANGE};--purple:{PURPLE};}} *{{box-sizing:border-box}} body{{margin:0;background:#fffefa;color:#1b1b1b;font:16px/1.6 system-ui,Arial,sans-serif}}
header{{background:#fff5d6;padding:34px max(calc((100vw - 1050px)/2),24px);border-bottom:5px solid var(--orange)}}h1{{font-size:clamp(27px,4vw,45px);line-height:1.1;margin:12px 0}}h2{{margin-top:36px}}main{{max-width:1100px;margin:auto;padding:16px 24px 60px}}.small{{color:#666;font-size:14px}}.pill{{display:inline-block;padding:4px 12px;background:var(--purple);color:#fff;border-radius:40px;font-size:13px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px}}.card{{background:white;border:1px solid #eee1cb;border-radius:14px;padding:18px}}.number{{font-size:29px;font-weight:800;color:var(--purple)}}table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{padding:9px 12px;border-bottom:1px solid #ece1cb;text-align:left}}th{{background:#fff5d6}}.scroll{{overflow:auto}}.note{{border-left:4px solid var(--orange);background:#fff5d6;padding:12px 16px;margin:20px 0}}img{{max-width:100%;height:auto}}a{{color:var(--purple)}}footer{{font-size:13px;color:#555;padding-top:25px}}
</style></head><body><header><span class="pill">Asociación Arrabal · Bootcamp Data Analyst</span><h1>Laboratorio de North Star y KPIs</h1>
<p>GoalZone · reservas deportivas · cálculo automático desde GitHub Actions</p></header><main>
<div class="cards"><div class="card"><div class="small">Reservas válidas</div><div class="number">{kpi['reservas_elegibles']:,}</div></div>
<div class="card"><div class="small">Asistencias</div><div class="number">{kpi['asistencias_confirmadas']:,}</div></div>
<div class="card"><div class="small">Tasa de asistencia</div><div class="number">{rate:.1%}</div></div>
<div class="card"><div class="small">IC Wilson 95 %</div><div class="number" style="font-size:21px">{kpi['tasa_ic95_inf']:.1%}–{kpi['tasa_ic95_sup']:.1%}</div></div></div>
<h2>Asistencia por antigüedad</h2><p>Selecciona una categoría de clase y explora los intervalos de confianza y el tamaño muestral de cada segmento.</p>
{plot_html}
<h2>Árbol de métricas</h2><img src="metric_tree.png" alt="Árbol de KPIs con coeficientes y q-values">
<div class="note"><strong>Atención:</strong> el gráfico representa asociaciones exploratorias. Ni el árbol ni las correlaciones demuestran causalidad.</div>
<h2>Asociaciones con la asistencia</h2><div class="scroll"><table><tr><th>Variable</th><th>Contraste</th><th>Coeficiente</th><th>n</th><th>q ajustado</th></tr>{rows}</table></div>
<p class="small">El coeficiente r punto-biserial y la V de Cramér no deben compararse directamente por magnitud. V no tiene signo.</p>
<h2>Datos y recursos</h2><p><a href="presentacion.pdf">Presentación (PDF)</a> · <a href="correlaciones.csv">CSV de correlaciones</a> · <a href="segmentos_antiguedad.csv">CSV por antigüedad</a></p>
<p class="small">Fuente del dataset: <a href="{escape(source, quote=True)}">CSV público GoalZone</a>. Es un caso docente; sin identificador de usuario no podemos medir recurrencia ni una North Star semanal.</p>
<footer>Arrabal · Material didáctico · Última generación automática con GitHub Actions</footer></main></body></html>'''


def run(input_csv: Path | None = None, output: Path | None = None) -> dict:
    output = (output or REPO / "resultados").resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / "site").mkdir(exist_ok=True)
    path = input_csv if input_csv is not None else output / "origen" / "fitness_class_2212.csv"
    if input_csv is None:
        source = download_csv(path)
    else:
        source = f"Archivo proporcionado: {path.name}"
    raw = pd.read_csv(path, dtype={"booking_id": "string"})
    df, quality = clean_goalzone(raw)
    kpi, corr = compute_metrics(df)
    if not kpi["reservas_elegibles"]:
        raise ValueError("Sin reservas válidas para calcular KPI")
    df.to_csv(output / "datos_limpios.csv", index=False)
    corr.to_csv(output / "correlaciones.csv", index=False)
    by_tenure = segment_rates(df, "tenure_group")
    by_tenure.to_csv(output / "segmentos_antiguedad.csv", index=False)
    for col, suffix in (("category", "categoria"), ("time", "horario"), ("day_of_week_normalized", "dia")):
        segment_rates(df, col).to_csv(output / f"segmentos_{suffix}.csv", index=False)
    summary = {"fuente": source, "kpi": kpi, "calidad": quality}
    (output / "resumen.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    (output / "reporte.md").write_text(create_report(df, kpi, corr, quality, source), encoding="utf-8")
    tree_path = output / "site" / "metric_tree.png"
    plot_tree(corr, tree_path)
    fig = make_interactive_figure(df)
    (output / "site" / "index.html").write_text(html_report(kpi, corr, quality, fig, source), encoding="utf-8")
    shutil.copy2(output / "correlaciones.csv", output / "site" / "correlaciones.csv")
    shutil.copy2(output / "segmentos_antiguedad.csv", output / "site" / "segmentos_antiguedad.csv")
    slide = REPO / "slides" / "presentacion_kpis_arrabal.pdf"
    if slide.exists():
        shutil.copy2(slide, output / "site" / "presentacion.pdf")
    print(f"GoalZone: {len(df)} reservas; tasa={kpi['tasa_asistencia']:.2%}; resultados={output}")
    print(corr[["nombre", "metodo", "coeficiente", "n", "q_value_bh"]].to_string(index=False))
    return {"data": df, "quality": quality, "kpi": kpi, "correlations": corr, "site": output / "site" / "index.html"}


def main() -> None:
    p = argparse.ArgumentParser(description="Arrabal · KPI Lab GoalZone (ejecución completa en la nube)")
    p.add_argument("--input", type=Path, default=None, help="CSV alternativo para comprobación/offline")
    p.add_argument("--output", type=Path, default=None, help="Directorio de resultados")
    args = p.parse_args()
    run(args.input, args.output)


if __name__ == "__main__":
    main()
