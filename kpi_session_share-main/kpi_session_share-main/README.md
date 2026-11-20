

# Del ejemplo cotidiano a la North Star

**Arrabal / Somos F5 · Bootcamp Data Analyst · 40 minutos**  
**Presentación · Actividades · Guía docente · Laboratorio reproducible en la nube**
</div>

> **Pregunta de apertura:** ¿estamos midiendo actividad o valor para el usuario?

## Materiales de la sesión

| Recurso | Contenido |
|---|---|
| [Presentación (PDF)](slides/presentacion_kpis_arrabal.pdf) | 8 diapositivas para introducir ejemplos y generar debate. |
| [Actividad 1: debate](actividades/01_debate_inicial.md) | Spotify, gimnasio y reparto a domicilio. |
| [Actividad 2: North Star](actividades/02_reto_goalzone.md) | Construcción del árbol de métricas de GoalZone. |
| [Plantilla del equipo](actividades/plantilla_equipo.md) | Entregable reproducible del grupo. |
| [Actividad 3: análisis](actividades/03_extension_datos.md) | Extensión opcional para interpretar correlaciones. |
| [Notebook de solución](lab/Solucion_GoalZone_Colab.ipynb) | Ejecutable en Google Colab, sin instalación local. |
| [Script de análisis](lab/analisis.py) | Descarga datos, calcula KPIs y genera gráficos e informe. |

## Sesión de 40 minutos

| Minutos | Actividad | Entrega |
|---|---|---|
| 0–10 | Ejemplos cotidianos y debate (slides 1–4) | Argumentar actividad frente a valor |
| 10–20 | North Star, KPIs de palanca y checklist (5–6) | Selección razonada de métricas |
| 20–35 | Equipos: árbol GoalZone (7) | [Plantilla completada](actividades/plantilla_equipo.md) |
| 35–40 | Puesta en común y puente a datos (8) | Crítica de las propuestas |

El laboratorio es **una demostración preejecutada o actividad de ampliación**: no depende de terminar una ejecución de GitHub durante los 40 minutos.

## Ejecutar el laboratorio sin instalar Python

### GitHub Actions: informe automático

1. Sube **todo el contenido de este repositorio** a la raíz de GitHub, incluida `.github/workflows/`.
2. Abre **Actions → Arrabal · ejecutar laboratorio GoalZone → Run workflow**.
3. Al terminar, descarga el artefacto **`analisis-goalzone`**.
4. Descomprímelo y abre `site/index.html`. Incluye el gráfico Plotly interactivo, el árbol, el informe y los CSV de resultados.

El workflow instala dependencias, comprueba el código, descarga el CSV público de GoalZone, ejecuta el análisis y guarda los resultados. Puede fallar si la fuente externa no está disponible. **No sustituye datos ausentes por datos sintéticos**.

### Google Colab: notebook interactivo

1. Abre [Google Colab](https://colab.research.google.com/).
2. Elige **Archivo → Abrir cuaderno → GitHub**, introduce la URL de este repositorio y abre `lab/Solucion_GoalZone_Colab.ipynb`.
3. Ejecuta **Entorno de ejecución → Ejecutar todo**. Se descargará el CSV directamente, sin rutas Windows.

Para publicar los resultados en una web GitHub Pages, consulta los comentarios de [`.github/workflows/analizar-goalzone.yml`](.github/workflows/analizar-goalzone.yml): el job `publicar` es opcional y requiere configurar la variable `PUBLISH_PAGES=true` y habilitar GitHub Pages desde Actions.

## Qué métricas se estudian

- **North Star conceptual:** personas que disfrutan de clases satisfactorias de manera recurrente. **No es observable** con este dataset.
- **Proxy observable:** tasa de asistencia por reserva, calculada a partir de `attended`.
- **Identidad de volumen:** asistencias = reservas elegibles × tasa de asistencia.
- **Asociaciones exploratorias:** antigüedad, días de antelación, categoría, horario y día de la semana.

Se utilizan r punto-biserial, V de Cramér y p-values ajustados por Benjamini–Hochberg, según la naturaleza de cada variable. **No se infiere causalidad a partir de las correlaciones.**

**Fuente:** [CSV docente GoalZone](https://raw.githubusercontent.com/xrander/fitness_class_project/master/fitness_class_2212.csv). No contiene `member_id` ni satisfacción y no permite calcular recurrencia semanal por usuario. La procedencia de datos operacionales reales no está acreditada.

## Estructura

```text
kpi_session/
├── .github/workflows/analizar-goalzone.yml
├── README.md
├── actividades/
│   ├── 01_debate_inicial.md
│   ├── 02_reto_goalzone.md
│   ├── 03_extension_datos.md
│   └── plantilla_equipo.md
├── slides/
│   ├── presentacion_kpis_arrabal.pdf
├── lab/
│   ├── analisis.py
│   └── Solucion_GoalZone_Colab.ipynb
├── tests/test_lab.py
├── requirements.txt
└── NOTICE.md
```



## Pruebas (solo mantenimiento, no requiere ejecución por alumnado)

```bash
python -m pip install -r requirements.txt
python -m pytest -q tests/
python lab/analisis.py --output resultados
```

El último comando descarga datos desde Internet y escribe los resultados en `resultados/` (ignorados por Git).

---
