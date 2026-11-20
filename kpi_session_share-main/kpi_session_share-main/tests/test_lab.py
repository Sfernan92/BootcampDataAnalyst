"""Pruebas sintéticas offline: NO son resultados del dataset original."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from lab.analisis import clean_goalzone, compute_metrics, run, wilson_interval


def mock_reservations(n=240):
    rng = np.random.default_rng(42)
    tenure = rng.integers(1, 35, size=n)
    probability = 0.15 + 0.7 * tenure / 35
    attendance = rng.binomial(1, probability, size=n)
    return pd.DataFrame({
        "booking_id": [f"{i:04d}" for i in range(n)],
        "months_as_member": tenure,
        "days_before": [f"{x} days" for x in rng.integers(1, 10, size=n)],
        "category": rng.choice(["Yoga", "Pilates", "HIIT"], size=n),
        "time": rng.choice(["AM", "PM"], size=n),
        "day_of_week": rng.choice(["Mon", "Tue", "Wed", "Thu", "Fri"], size=n),
        "attended": attendance,
    })


def test_wilson_interval():
    empty = wilson_interval(0, 0)
    assert np.isnan(empty[0]) and np.isnan(empty[1])
    lo, hi = wilson_interval(20, 30)
    assert 0 < lo < 20 / 30 < hi < 1


def test_clean_and_formula():
    raw = mock_reservations()
    clean, quality = clean_goalzone(raw)
    kpi, corrs = compute_metrics(clean)
    assert quality["filas_origen"] == 240
    assert kpi["asistencias_confirmadas"] == raw["attended"].sum()
    assert np.isclose(kpi["reservas_elegibles"] * kpi["tasa_asistencia"], kpi["asistencias_confirmadas"])
    assert len(corrs) == 5
    assert (corrs["q_value_bh"].dropna() <= 1).all()


def test_duplicate_ids_are_rejected():
    raw = mock_reservations()
    raw.loc[1, "booking_id"] = raw.loc[0, "booking_id"]
    with pytest.raises(ValueError, match="duplicado"):
        clean_goalzone(raw)


def test_missing_columns_rejected():
    raw = mock_reservations().drop(columns=["attended"])
    with pytest.raises(ValueError, match="incompleto"):
        clean_goalzone(raw)


def test_end_to_end_offline(tmp_path: Path):
    source = tmp_path / "example.csv"
    mock_reservations().to_csv(source, index=False)
    out = tmp_path / "output"
    result = run(input_csv=source, output=out)
    assert len(result["data"]) == 240
    for name in ["datos_limpios.csv", "correlaciones.csv", "segmentos_antiguedad.csv", "reporte.md", "resumen.json", "site/index.html", "site/metric_tree.png"]:
        assert (out / name).is_file(), name
    assert (out / "site/index.html").stat().st_size > 100_000  # Plotly integrado (sin CDN)
    obj = json.loads((out / "resumen.json").read_text(encoding="utf-8"))
    assert obj["kpi"]["reservas_elegibles"] == 240
