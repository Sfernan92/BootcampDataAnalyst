# Actividad 2 — Diseña el árbol de métricas

**Caso principal:** GoalZone, plataforma que organiza reservas de clases deportivas.

**Duración:** 15 minutos en grupos + 5 minutos de debate.

## Contexto

Una reserva no garantiza que la persona vaya a clase. GoalZone dispone de un dataset docente de **1.500 reservas** con una variable binaria `attended` (asistencia observada). Contiene antigüedad del socio, categoría de clase, horario, día y antelación de reserva. **No contiene identificador del socio ni una serie completa de eventos por persona.**

## Parte A — Definir el resultado

1. ¿Cuál sería la **North Star ideal** desde la perspectiva de quien reserva?
2. ¿Qué *proxy* podemos calcular con los datos disponibles? Explica por qué no equivalen.
3. Para la proxy, completa esta ficha:

| Elemento | Tu definición |
|---|---|
| Nombre de la métrica | |
| Valor para el usuario que representa | |
| Unidad de análisis | |
| Numerador | |
| Denominador | |
| Periodicidad | |
| Exclusiones (cancelaciones, nulos...) | |
| Limitaciones y sesgos | |

## Parte B — Árbol de métricas

Propón tres posibles inputs y distingue:
- **Palancas accionables:** factores sobre los que el equipo puede experimentar (p. ej. cambios de onboarding).
- **Descriptores/contexto:** características que podemos observar, pero no modificar directamente (p. ej. antigüedad).
- **Identidades contables:** multiplicaciones exactas entre métricas que no demuestran causalidad.

Rellena:

| KPI candidato | Unidad | ¿Accionable? | Hipótesis | Dato necesario |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Parte C — Una predicción que pueda refutarse

> Si cambiamos **________** para las personas **________**, esperamos que aumente **________** sin deteriorar **________**. Lo verificaríamos con **________**.

## Debate después de abrir el informe

- ¿Qué variable tiene una asociación más clara con `attended`? ¿Eso la convierte en una palanca?
- ¿Qué significa que una prueba no resulte significativa?
- ¿Cómo distinguir correlación, relación aritmética y efecto causal?

**Entrega del equipo:** definición operativa, diagrama con 3 inputs, una limitación de datos y una hipótesis comprobable. No hace falta programar.
