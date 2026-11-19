# Informe de laboratorio · GoalZone

> **Datos docentes públicos**, no evidencia auditada de operaciones reales de una empresa.

**Fuente CSV:** https://raw.githubusercontent.com/xrander/fitness_class_project/master/fitness_class_2212.csv

## KPI observable

- Reservas elegibles: **1,500**
- Asistencias confirmadas: **454**
- Tasa de asistencia: **30.3%**
- IC Wilson del 95 %: **[28.0%; 32.6%]**

**Identidad aritmética:** asistencias = reservas elegibles × tasa de asistencia.
Esta identidad no es evidencia causal de una palanca.

## Calidad del dato

- filas origen: 1500
- reservas con target valido: 1500
- reservas sin target valido: 0
- ids duplicados: 0
- nulos antiguedad: 0
- nulos anticipacion: 0
- nulos categoria: 13
- nulos dia normalizado: 0

## Asociaciones con `attended`

| Variable | Método | Coeficiente | n | q BH |
|---|---|---:|---:|---:|
| Antigüedad del socio | r punto-biserial | 0.4855 | 1500 | 7.505e-89 |
| Antelación de reserva | r punto-biserial | 0.02407 | 1500 | 0.4395 |
| Categoría de clase | V de Cramér (sin signo) | 0.04349 | 1487 | 0.5896 |
| Horario | V de Cramér (sin signo) | 0.04985 | 1500 | 0.1338 |
| Día de la semana | V de Cramér (sin signo) | 0.06808 | 1500 | 0.4395 |

**Lectura:** q de Benjamini–Hochberg < 0,05 indica una asociación exploratoria significativa, no causalidad.
El coeficiente r punto-biserial tiene signo; V de Cramér carece de signo y no es comparable directamente con r.

## Limitaciones

- Grano del dataset: **reserva**, no socio. No hay un ID de persona que permita medir recurrencia.
- La asistencia no demuestra que la clase haya sido satisfactoria.
- La antigüedad puede mostrar sesgo de supervivencia: quienes persisten podrían ser quienes ya participaban más.
- Las asociaciones bivariadas no controlan confusores ni prueban que cambiar un input cambie la North Star.
- Faltan fechas individuales completas para obtener una North Star semanal real.

## Pregunta de discusión

> Si la antigüedad muestra asociación con la asistencia, ¿es una palanca sobre la que producto pueda actuar hoy?

Propuesta contrastable: experimentar con mejoras de onboarding y medir asistencia temprana y retención posterior.
