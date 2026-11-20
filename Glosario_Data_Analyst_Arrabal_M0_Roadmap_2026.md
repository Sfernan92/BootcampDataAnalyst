# Glosario de negocio y tecnología — Bootcamp Data Analyst

**Arrabal / Somos F5 · Edición para el alumnado · 19/11/2026 · Versión 1.0**

## Cómo utilizar este glosario

El glosario sigue el itinerario competencial del bootcamp: **mentalidad de ingeniería de datos → análisis de negocio/BI → validación estadística/Data Science**. Los términos en **NÚCLEO M0** están alineados con las primeras actividades de herramientas, Roomscape, Python, Git/GitHub y negocio (KPI/North Star); **incluyen también nociones que se introducirán o consolidarán a lo largo de M0, y no implican que todas estén ya impartidas o evaluadas**. Los términos en **AMPLIACIÓN** son vocabulario previsto progresivamente en módulos posteriores.

> **Convención:** las traducciones al español son orientativas; conviene reconocer también los términos originales en inglés. Los ejemplos y los números son didácticos, no resultados observados de empresas reales ni del dataset de clase.

## Selección prioritaria para las primeras sesiones

**Negocio y métricas (12):** dato, métrica, KPI, objetivo de negocio, North Star Metric, métrica de vanidad, guardrail, árbol de métricas, numerador, denominador, tasa de conversión, baseline.

**Herramientas y colaboración (12):** terminal, shell, CLI, directorio de trabajo, Git Bash, VS Code, intérprete, repositorio, Git, GitHub, commit, README.

**Python (8):** variable, tipo de dato, `int`, `float`, `str`, `bool`, lista, condicional.

**Próximas nociones a consolidar (8):** unidad de análisis, granularidad, escalas de medida, función, Pull Request, notebook, CI y test automatizado. La prioridad exacta dependerá del avance real de las prácticas.

---

# PARTE I — NÚCLEO M0: vocabulario de las primeras sesiones

## 1. Negocio, producto y toma de decisiones

| Término | Definición para Data Analysts | Ejemplo práctico |
|---|---|---|
| **Negocio (business)** | Organización o actividad que ofrece valor a unas personas y necesita sostener sus operaciones. | Una plataforma gestiona reservas de instalaciones deportivas. |
| **Modelo de negocio (business model)** | Forma de crear, entregar y, en su caso, capturar valor. | Cobrar una comisión por reserva gestionada. |
| **Propuesta de valor (value proposition)** | Beneficio concreto que recibe el usuario o cliente. | Encontrar y reservar una pista sin llamadas. |
| **Stakeholder / parte interesada** | Persona o grupo afectado por un proyecto o que toma decisiones sobre él. | Alumnado, usuarios, equipo de producto, responsables de negocio. |
| **Cliente (customer)** | Quien contrata, paga o financia un producto o servicio; no siempre coincide con quien lo usa. | Un ayuntamiento financia una actividad utilizada por familias. |
| **Usuario (user)** | Persona que utiliza el servicio. | Alguien que reserva una pista en una aplicación. |
| **Objetivo de negocio (business objective)** | Resultado que se desea conseguir, expresado de forma comprensible y medible. | Reducir el abandono en el proceso de reserva. |
| **Pregunta de negocio (business question)** | Pregunta concreta que puede contestarse con información y orientar una decisión. | ¿En qué paso se pierden más reservas? |
| **Hipótesis de negocio** | Explicación o predicción que es posible contrastar. | Reducir los campos del formulario aumentará las reservas completadas. |
| **Insight / hallazgo accionable** | Interpretación respaldada por datos que ayuda a decidir; no es simplemente una cifra. | La mayoría de abandonos ocurre al solicitar el pago. |
| **Decisión (decision)** | Acción elegida a partir de objetivos, evidencia y restricciones. | Probar un proceso de pago más sencillo. |
| **Impacto (impact)** | Cambio real atribuible, o razonablemente vinculado con cautela, a una intervención. | Mejora de la inserción laboral verificada meses después de un programa. |
| **Output / actividad producida** | Entrega o actividad realizada; no demuestra por sí sola un resultado final. | Número de personas que terminaron un taller. |
| **Outcome / resultado conseguido** | Cambio observado en la situación o comportamiento de las personas. | Personas que acceden a un empleo después de un itinerario. |
| **Facturación (revenue)** | Ingresos por ventas o prestación de servicios, antes de descontar costes. | 100 reservas × 10 € = 1.000 € de ventas. |
| **Coste (cost)** | Recursos consumidos para ofrecer un servicio. | Comisiones, atención al cliente, infraestructura. |
| **Beneficio (profit)** | Diferencia entre ingresos y costes, según el alcance contable definido. | 1.000 € de ingresos y 700 € de costes: 300 € de beneficio. |
| **ROI (Return on Investment)** | Rentabilidad relativa de una inversión; es necesario definir costes y beneficios incluidos. | (Beneficio neto de inversión / coste de inversión) × 100. |

## 2. Métricas, KPI y North Star (imprescindible)

| Término | Definición para Data Analysts | Ejemplo práctico |
|---|---|---|
| **Dato (data)** | Registro o valor bruto, aún sin interpretar. | Una reserva tiene fecha 18/11 y estado «confirmada». |
| **Métrica (metric)** | Medida cuantitativa, con una definición y una regla de cálculo. | Número de reservas confirmadas cada semana. |
| **Indicador (indicator)** | Medida utilizada para describir un aspecto de un proceso u objetivo; puede ser o no un KPI. | Porcentaje de personas que completan un formulario. |
| **KPI (Key Performance Indicator)** | Indicador clave elegido para evaluar un objetivo prioritario de negocio, con definición, frecuencia y responsable. | % de reservas completadas de las que se inician. |
| **North Star Metric (NSM)** | Métrica principal que intenta reflejar el valor que reciben los usuarios y guiar el crecimiento sostenible del producto. | Reservas efectivamente disfrutadas por semana, **si existe evidencia de uso**. |
| **Proxy / indicador indirecto** | Medida sustitutiva utilizada cuando el fenómeno importante no se observa directamente. | Reservas confirmadas como proxy de reservas disfrutadas. |
| **KPI operativo** | Indicador que ayuda a supervisar procesos concretos. | Tiempo medio hasta confirmar una reserva. |
| **Métrica de vanidad (vanity metric)** | Medida que impresiona pero no prueba creación de valor ni orienta una buena decisión. | Descargas totales de la app sin comprobar uso. |
| **Métrica accionable (actionable metric)** | Medida vinculable a una decisión o intervención específica. | Abandono en el paso de pago. |
| **Leading indicator / indicador adelantado** | Señal temprana que puede anticipar un resultado futuro; hay que validar esa relación. | Porcentaje de usuarios que llegan al paso final del proceso. |
| **Lagging indicator / indicador rezagado** | Resultado observado después de que transcurra el proceso. | Reservas finalmente completadas del mes. |
| **Guardrail metric / métrica de protección** | Indicador que limita cambios no deseados mientras se optimiza otro. | Incidencias por 100 reservas o tasa de cancelaciones. |
| **Árbol de métricas (metric tree)** | Descomposición de un objetivo en factores medibles que explican cómo se alcanza. | Reservas = visitantes × tasa de inicio × tasa de finalización (con poblaciones compatibles). |
| **Objetivo (goal)** | Resultado deseado; diferente de la cifra que lo representa. | Mejorar la experiencia de reserva. |
| **Meta (target)** | Valor concreto que se pretende alcanzar en una fecha. | Alcanzar un 65 % de finalización en diciembre. |
| **Baseline / línea base** | Valor de referencia previo a una intervención. | Finalización actual: 52 %. |
| **Benchmark / referencia externa** | Valor o desempeño con el que se compara una métrica. | Tasa comparable de otro producto, si mide lo mismo. |
| **Numerador** | Parte superior de una razón o tasa. | Reservas completadas. |
| **Denominador** | Población o conjunto respecto al que se calcula una razón. | Reservas iniciadas. |
| **Ratio / razón** | Cociente entre dos cantidades. | 70 reservas / 100 intentos = 0,7. |
| **Tasa (rate)** | Medida relativa respecto a una población, eventos o tiempo; debe declararse el denominador. | 70 reservas completadas por cada 100 iniciadas. |
| **Porcentaje** | Razón multiplicada por 100; indica partes de cada cien. | 0,7 × 100 = 70 %. |
| **Punto porcentual (pp)** | Diferencia absoluta entre porcentajes. | Pasar de 50 % a 55 % son +5 pp, no +5 %. |
| **Variación relativa** | Cambio expresado respecto al valor inicial. | De 50 % a 55 % equivale a +10 % relativo. |
| **Segmentación** | Separación de datos por grupos con características relevantes. | Reservas por canal de adquisición o tipo de pista. |
| **Funnel / embudo** | Secuencia de pasos por la que pasan usuarios o eventos. | Visita → búsqueda → inicio de reserva → confirmación. |
| **Conversión (conversion)** | Ocurrencia de la acción definida como objetivo. | Pasar de intento de reserva a reserva confirmada. |
| **Tasa de conversión** | Conversiones divididas entre la población elegible, indicando la ventana temporal. | 60 confirmaciones / 100 inicios = 60 %. |
| **Retención (retention)** | Proporción de una cohorte que vuelve o permanece activa según un criterio y periodo. | Usuarios de octubre que reservan de nuevo en noviembre. |
| **Churn / abandono** | Proporción de clientes o usuarios que dejan de estar activos bajo una regla explícita. | Suscriptores que cancelan durante el mes / suscriptores al inicio. |
| **Cohorte (cohort)** | Grupo definido por compartir un evento o característica en un periodo. | Usuarios que hicieron su primera reserva en octubre. |
| **Engagement / implicación** | Frecuencia o profundidad de interacción con el producto; debe especificarse cómo se mide. | Reservas realizadas por usuario activo al mes. |
| **DAU / WAU / MAU** | Usuarios activos diarios, semanales o mensuales según un criterio consistente. | MAU: usuarios que completaron ≥1 acción válida en el mes. |
| **ARPU** | Ingreso medio por usuario en un periodo; requiere definir la base de usuarios. | Ingresos del mes / usuarios de referencia del mes. |
| **CAC** | Coste medio de adquirir un cliente, según los costes y clientes incluidos. | Gasto comercial y marketing / nuevos clientes adquiridos. |
| **LTV / CLV** | Estimación del valor económico que aporta un cliente durante su relación con la organización. | Margen esperado por cliente a lo largo de su ciclo de vida. |

### Caso transversal: KPI frente a North Star

Una plataforma de reservas deportivas persigue **facilitar que las personas practiquen deporte**:

- **Objetivo de negocio:** que más reservas terminen en una actividad real, sin deteriorar el servicio.
- **North Star ideal:** sesiones deportivas efectivamente disfrutadas por semana. Solo es medible si hay registros de asistencia o uso.
- **North Star proxy:** reservas confirmadas por semana, si todavía no se observa el disfrute real.
- **KPIs impulsores:** usuarios que inician reserva, tasa de finalización, reservas recurrentes.
- **Guardrails:** tasa de cancelaciones, reclamaciones y tiempos de espera.
- **Métrica de vanidad potencial:** visitas a la web, si crecen pero las reservas útiles no.

**Error que debemos evitar:** un KPI no es «cualquier número del dashboard»; la North Star no es «el KPI más grande»; y una mejora de porcentaje no equivale necesariamente a una mejora de impacto.

## 3. Fundamentos de datos, variables y medición (ST1/ST2)

| Término | Definición para Data Analysts | Ejemplo práctico |
|---|---|---|
| **Población** | Conjunto completo de elementos de interés. | Todas las reservas de un año. |
| **Muestra** | Subconjunto observado de una población. | 300 reservas seleccionadas para análisis. |
| **Unidad de análisis** | Entidad sobre la que se quiere concluir algo. | Usuario, reserva, curso o programa. |
| **Observación / registro** | Caso individual registrado en el dataset. | Una fila con una reserva concreta. |
| **Variable** | Característica que puede tomar valores distintos entre observaciones. | Canal, edad, precio, estado de reserva. |
| **Variable cualitativa** | Describe categorías, no cantidades aritméticas. | Canal de adquisición. |
| **Variable cuantitativa** | Representa una cantidad numérica. | Número de reservas por usuario. |
| **Escala nominal** | Categorías sin orden intrínseco. | Web, app, teléfono. |
| **Escala ordinal** | Categorías con orden, pero distancias no cuantificadas de forma uniforme. | Satisfacción baja, media, alta. |
| **Escala de intervalo** | Valores con diferencias comparables, pero sin cero absoluto. | Temperatura en grados Celsius. |
| **Escala de razón** | Valores con cero absoluto y cocientes interpretables. | Ingresos, duración, número de reservas. |
| **Variable discreta** | Variable numérica que toma valores contables separados. | Número de entradas vendidas. |
| **Variable continua** | Variable numérica que puede tomar valores en un intervalo. | Duración de una sesión medida con precisión. |
| **Variable booleana / binaria** | Toma dos estados; puede codificarse `True/False` o `0/1`. | ¿Reserva cancelada? |
| **Granularidad / grano (grain)** | Nivel de detalle representado por cada fila. | Una fila por reserva vs. una fila por usuario y mes. |
| **Identificador (ID)** | Valor que permite distinguir una entidad. | `reservation_id`. |
| **Nulo / valor ausente** | Información no registrada o no disponible; no equivale necesariamente a cero. | Fecha de cancelación vacía si no se canceló. |
| **Valor atípico (outlier)** | Observación muy alejada del comportamiento habitual; puede ser legítima o un error. | Una reserva de 500 horas de duración. |
| **Sesgo (bias)** | Distorsión sistemática de medición, selección o análisis. | Medir solo usuarios de la app y omitir reservas telefónicas. |

## 4. Herramientas, terminal, Git y colaboración (Roomscape)

| Término | Definición para Data Analysts | Ejemplo práctico |
|---|---|---|
| **Sistema operativo (OS)** | Software base que administra el equipo y ejecuta aplicaciones. | Windows. |
| **Terminal** | Interfaz en la que se escriben comandos de texto. | Consola integrada de VS Code. |
| **Shell** | Programa que interpreta los comandos de la terminal. | PowerShell o Bash. |
| **CLI (Command-Line Interface)** | Forma de interactuar con programas mediante comandos. | Ejecutar `python --version`. |
| **GUI (Graphical User Interface)** | Interfaz visual con ventanas y botones. | GitHub Desktop. |
| **PowerShell** | Shell y entorno de automatización de Microsoft. | `Get-Location`. |
| **Git Bash** | Entorno Bash distribuido con Git para Windows. | `pwd`, `ls` y `git status`. |
| **Directorio / carpeta** | Contenedor de archivos y otras carpetas. | Carpeta `proyecto/`. |
| **Ruta absoluta / relativa** | Ubicación completa desde una raíz / ubicación respecto a la carpeta actual. | `C:\datos\ventas.csv` / `datos/ventas.csv`. |
| **Directorio de trabajo (working directory)** | Carpeta desde la que se ejecuta un comando. | Verla con `pwd` en Bash. |
| **Editor de código** | Aplicación para escribir y modificar archivos de programación. | VS Code o Sublime Text. |
| **IDE** | Entorno que integra edición, ejecución, depuración y otras herramientas. | VS Code configurado para Python. |
| **Intérprete** | Programa que ejecuta el código de un lenguaje como Python. | Python 3.x. |
| **Extensión (extension)** | Complemento que añade funciones a una aplicación. | Extensión Python de VS Code. |
| **Jupyter Notebook** | Documento con celdas de código y texto ejecutables de manera interactiva. | `analisis.ipynb`. |
| **Google Colab** | Servicio en la nube para ejecutar notebooks de Python. | Abrir un notebook sin instalar librerías localmente. |
| **Celda Markdown** | Parte de un notebook para explicar pasos, decisiones o resultados. | Documentar una hipótesis antes de calcular. |
| **Repositorio (repository / repo)** | Carpeta de proyecto gestionada por un sistema de control de versiones. | Repositorio público de prácticas del equipo. |
| **Git** | Sistema distribuido que registra versiones del código y los archivos. | Guardar el historial de un ejercicio. |
| **GitHub** | Plataforma de alojamiento y colaboración sobre repositorios Git. | Compartir una práctica con el equipo. |
| **Clone / clonar** | Copiar un repositorio remoto a un equipo local. | `git clone URL`. |
| **Commit** | Registro identificado de un conjunto de cambios en Git. | «Añadir solución de ejercicio 1». |
| **Branch / rama** | Línea paralela de trabajo dentro de un repositorio. | `feature/kpi`. |
| **Push** | Enviar commits locales al repositorio remoto. | `git push`. |
| **Pull** | Obtener e integrar cambios del repositorio remoto en la rama local. | `git pull`. |
| **Pull Request (PR)** | Propuesta de integrar cambios, normalmente con revisión. | El equipo revisa una solución antes de fusionarla. |
| **Merge / fusionar** | Combinar historias o cambios de distintas ramas. | Incorporar una PR aprobada a `main`. |
| **README** | Archivo introductorio que explica propósito, requisitos y pasos de uso. | Cómo ejecutar el ejercicio y su objetivo. |
| **`.gitignore`** | Archivo de patrones que indican qué archivos no debe seguir Git. | Evitar subir entornos virtuales y archivos temporales. |
| **Conflicto de merge** | Situación en la que Git no puede integrar automáticamente cambios incompatibles. | Dos personas modifican la misma línea. |
| **Workflow / flujo de trabajo** | Secuencia organizada de pasos; en GitHub Actions, automatización definida en YAML. | Comprobar un notebook al subir cambios. |
| **CI (Continuous Integration)** | Integración continua: validar cambios con pruebas y controles automáticos. | Ejecutar tests cuando se abre una PR. |
| **CD (Continuous Delivery/Deployment)** | Entrega o despliegue continuo: preparar o publicar versiones de forma automatizada. | Publicar un informe tras las comprobaciones. |
| **GitHub Actions** | Servicio para ejecutar workflows en repositorios GitHub. | Validación automática tras un `push`. |
| **Artifact / artefacto** | Archivo generado por una ejecución que se conserva como resultado descargable. | CSV limpio o informe producido por un workflow. |
| **Log** | Registro de mensajes y eventos de una ejecución. | Ver por qué falló un workflow. |
| **Test / prueba automatizada** | Comprobación reproducible de que una regla o conducta se cumple. | El porcentaje calculado debe estar entre 0 y 100. |
| **Reproducibilidad** | Capacidad de obtener resultados equivalentes usando los mismos datos, código y condiciones. | Otra persona ejecuta el notebook siguiendo el README. |

**Nota de secuenciación:** Git y los repositorios forman parte de los fundamentos. CI/CD y GitHub Actions pueden aparecer en una demostración o práctica inicial, pero su estudio sistemático corresponde al bloque de ingeniería/automatización del roadmap.

## 5. Python fundamental

| Término | Definición para Data Analysts | Ejemplo práctico |
|---|---|---|
| **Script** | Archivo de código que ejecuta una serie de instrucciones. | `calcular_kpi.py`. |
| **Sintaxis** | Reglas formales para escribir código válido. | `if x > 0:` seguido de bloque indentado. |
| **Variable (Python)** | Nombre al que se asigna un objeto/valor durante la ejecución; distinto del concepto estadístico. | `reservas = 120`. |
| **Tipo de dato** | Clase de valor y operaciones disponibles. | `int`, `float`, `str`, `bool`. |
| **`int` / `float`** | Entero / número de coma flotante. | `23`, `0.75`. |
| **`str` / cadena** | Secuencia de caracteres de texto. | `"confirmada"`. |
| **`bool`** | Tipo lógico: verdadero o falso. | `True`, `False`. |
| **`None`** | Valor especial que expresa ausencia de valor en Python. | `fecha_baja = None`. |
| **Lista (`list`)** | Colección ordenada y modificable. | `[10, 12, 15]`. |
| **Diccionario (`dict`)** | Colección de pares clave-valor. | `{"reservas": 120}`. |
| **Índice** | Posición de un elemento en una secuencia; Python comienza en cero. | `precios[0]`. |
| **Operador** | Símbolo que realiza una operación. | `+`, `*`, `==`, `>=`. |
| **Condicional** | Ejecución de instrucciones según una condición. | `if reservas > 0:`. |
| **Bucle (`for` / `while`)** | Repetición de instrucciones. | Recorrer una lista de precios. |
| **Función** | Bloque reutilizable que recibe argumentos y puede devolver resultados. | `def conversion(completadas, iniciadas):`. |
| **Parámetro / argumento** | Nombre de entrada declarado por una función / valor que se le proporciona al llamarla. | `iniciadas` / `100`. |
| **`return`** | Instrucción que devuelve un resultado desde una función. | `return completadas / iniciadas`. |
| **Módulo / librería** | Archivo de Python reutilizable / conjunto de módulos o paquetes. | `import math`; más adelante `pandas`. |
| **Dependencia** | Paquete externo que necesita un proyecto. | `pandas` para analizar tablas. |
| **`pip`** | Herramienta para instalar paquetes Python. | `python -m pip install pandas`. |
| **Entorno virtual (`venv`)** | Aislamiento de dependencias para un proyecto. | Dos proyectos pueden usar versiones distintas. |
| **Error / excepción** | Problema detectado durante la ejecución que puede detenerla o gestionarse. | División por cero. |
| **Traceback** | Informe que muestra dónde se produjo una excepción. | Localizar el archivo y la línea del error. |

---

# PARTE II — AMPLIACIÓN PROGRESIVA: términos previstos en el roadmap

## 6. Ingeniería de datos: fuentes, calidad y almacenamiento (M1/M6)

| Término | Definición | Ejemplo |
|---|---|---|
| **Fuente de datos (data source)** | Sistema o archivo del que procede información. | Formulario, CSV, API, base de datos. |
| **Dataset** | Conjunto organizado de datos para un propósito. | Tabla de reservas de noviembre. |
| **CSV / JSON / JSONL** | Formatos para intercambiar datos tabulares o estructurados. | Reservas en CSV, respuestas API en JSON. |
| **API** | Interfaz que permite que dos programas intercambien información de forma controlada. | Consultar reservas desde una API autorizada. |
| **Evento (event)** | Registro de algo ocurrido en un instante o periodo. | `booking_confirmed`. |
| **Log de aplicación** | Registro técnico de funcionamiento y errores. | Fallo al procesar un pago. |
| **Web analytics** | Medición de interacciones en sitios o aplicaciones. | Visitas, clics, navegación y conversiones. |
| **Datos transaccionales** | Registros de operaciones concretas del negocio. | Pedidos, pagos, reservas. |
| **Ingesta (ingestion)** | Entrada de datos desde una fuente hacia otro sistema. | Descargar diariamente datos de una API. |
| **Pipeline de datos** | Secuencia organizada de adquisición, transformación y validación. | API → limpieza → tabla analítica. |
| **ETL / ELT** | Extraer, transformar y cargar / extraer, cargar y transformar. | Preparar datos antes o después de almacenarlos. |
| **Esquema (schema)** | Definición de campos, tipos y estructura de datos. | `fecha: date`, `importe: decimal`. |
| **Clave primaria (primary key)** | Campo o conjunto de campos que identifica de forma única cada fila de una tabla. | `reservation_id`. |
| **Clave foránea (foreign key)** | Campo que referencia una clave en otra tabla. | `user_id` en reservas. |
| **Duplicado** | Registro repetido de acuerdo con una clave/regla; no toda coincidencia es un error. | Mismo `reservation_id` recibido dos veces. |
| **Calidad de datos (data quality)** | Grado en que los datos sirven a su uso previsto. | Completitud, validez, unicidad, consistencia y actualidad. |
| **Validación de datos** | Comprobaciones de reglas y restricciones. | El importe no puede ser negativo. |
| **Data contract / contrato de datos** | Acuerdo entre productor y consumidor sobre estructura, significado y calidad. | `importe` numérico y `reservation_id` único. |
| **Linaje (data lineage)** | Trazabilidad del origen y las transformaciones de un dato. | Saber de qué fuente proviene un KPI. |
| **Diccionario de datos** | Documento que define columnas, significado, tipos y reglas de cálculo. | Qué significa exactamente `cliente_activo`. |
| **Data lake / data warehouse** | Almacén flexible de datos de múltiples formatos / repositorio optimizado para análisis estructurado. | Datos fuente vs. modelos analíticos curados. |
| **Arquitectura Medallion** | Organización por capas: Bronze (ingesta), Silver (depuración), Gold (datos de consumo). | Eventos originales → limpios → KPI semanal. |
| **Streaming / batch** | Procesar eventos según llegan / procesarlos por lotes. | Evento instantáneo / informe nocturno. |
| **Observabilidad** | Capacidad de comprender el estado de un sistema mediante logs, métricas y trazas. | Identificar una ingesta que dejó de actualizarse. |
| **Idempotencia** | Propiedad de una operación que, repetida, no produce efectos adicionales no deseados. | Reprocesar un día sin duplicar reservas. |

## 7. SQL, modelado y BI (M1/M4)

| Término | Definición | Ejemplo |
|---|---|---|
| **SQL** | Lenguaje de consulta y manipulación de datos relacionales. | `SELECT COUNT(*) FROM reservas;`. |
| **Tabla / fila / columna** | Estructura de registros y campos. | Tabla de usuarios con una fila por usuario. |
| **`SELECT` / `WHERE`** | Elegir columnas / filtrar registros. | Reservas confirmadas. |
| **`GROUP BY` / agregación** | Agrupar filas y calcular resúmenes. | Reservas por mes. |
| **`JOIN`** | Combinar tablas usando claves relacionadas. | Reservas y usuarios. |
| **`LEFT JOIN`** | Mantener las filas de la izquierda aunque no tengan correspondencia. | Todos los usuarios, hayan reservado o no. |
| **CTE** | Subconsulta con nombre (`WITH`) para estructurar consultas. | Preparar un cálculo por etapas. |
| **Función de ventana** | Cálculo entre filas relacionadas sin colapsar las observaciones. | Ordenar reservas dentro de cada usuario. |
| **Tabla de hechos** | Almacena eventos medibles al grano declarado. | Una fila por reserva, con importe. |
| **Tabla de dimensiones** | Describe entidades usadas para filtrar y segmentar. | Usuario, instalación, calendario. |
| **Modelo estrella** | Modelo analítico con una tabla de hechos conectada a dimensiones. | Reservas → fecha, usuario e instalación. |
| **BI (Business Intelligence)** | Prácticas y sistemas para transformar datos en información útil de gestión. | Seguir objetivos con un cuadro de mando. |
| **Dashboard / cuadro de mando** | Vista organizada de indicadores y tendencias para decidir. | Evolución semanal de reservas y abandonos. |
| **Data visualization** | Representación gráfica que facilita la interpretación. | Línea temporal, barras, dispersión. |
| **Storytelling con datos** | Relato estructurado de contexto, evidencia, limitaciones y recomendación. | Explicar por qué cambió la conversión. |
| **Power Query** | Motor/herramienta de importación y transformación de datos. | Tipificar y combinar tablas en Power BI. |
| **DAX** | Lenguaje de expresiones del modelo semántico de Power BI. | Medida de reservas confirmadas. |
| **Medida (measure)** | Cálculo evaluado en un contexto de filtros. | Tasa de conversión en Power BI. |
| **Modelo semántico** | Modelo que organiza tablas, relaciones y definiciones de negocio para análisis coherente. | Una definición compartida de usuario activo. |
| **Google Sheets** | Hoja de cálculo usada como apoyo para análisis y colaboración. | Tabla auxiliar o validación de cifras. |
| **Tableau / Tableau Public** | Herramientas de visualización; la versión Public publica contenido abierto. | Visualizaciones con datos públicos o sintéticos. |

**Herramientas del itinerario:** **Power BI** es la herramienta principal de BI; **Google Sheets**, auxiliar. Microsoft Excel y macros VBA no forman parte del itinerario técnico previsto en la revisión del programa.

## 8. Estadística, experimentación y Data Science (M2/M3)

| Término | Definición | Ejemplo |
|---|---|---|
| **EDA (Exploratory Data Analysis)** | Exploración sistemática para entender estructura, patrones y problemas de los datos. | Distribuir importes, buscar nulos y segmentar. |
| **Media / mediana** | Promedio aritmético / valor central de los datos ordenados. | Comparar tiempos típicos con y sin valores extremos. |
| **Percentil** | Valor bajo el que cae una proporción de observaciones. | P90 de espera: 90 % espera ese tiempo o menos. |
| **Desviación estándar** | Medida de dispersión alrededor de la media. | Variabilidad de tiempos de atención. |
| **Correlación** | Asociación estadística entre variables, sin demostrar causalidad. | Más visitas coinciden con más reservas. |
| **Causalidad** | Relación en la que un factor produce un cambio en otro, bajo supuestos adecuados. | Un cambio del formulario aumenta conversiones. |
| **Confusor** | Variable que afecta a la exposición y al resultado, distorsionando su relación. | Estacionalidad influye en publicidad y reservas. |
| **Inferencia estadística** | Uso de una muestra para razonar sobre una población con incertidumbre. | Estimar la conversión real de todos los usuarios. |
| **Intervalo de confianza** | Procedimiento que produce intervalos con cobertura nominal bajo repetición del muestreo y supuestos del modelo. | IC del 95 % para una tasa de conversión. |
| **Hipótesis nula / alternativa** | Afirmaciones formales contrastadas en una prueba estadística. | H0: las tasas son iguales; H1: difieren. |
| **Valor p (p-value)** | Probabilidad, bajo H0 y el modelo, de obtener resultados al menos tan extremos como los observados. | No es la probabilidad de que H0 sea verdadera. |
| **Tamaño del efecto** | Magnitud del cambio o asociación; complementa la significación estadística. | +3 puntos porcentuales de conversión. |
| **Potencia estadística** | Probabilidad de detectar un efecto especificado cuando realmente existe. | Planificar el tamaño de muestra. |
| **A/B testing** | Experimento que asigna aleatoriamente alternativas a unidades para medir su efecto. | Formulario A frente a B. |
| **Aleatorización (randomization)** | Asignación por azar que ayuda a equilibrar factores entre grupos. | Usuarios asignados a A o B. |
| **Muestreo** | Procedimiento de selección de observaciones. | Elegir reservas por semana y canal. |
| **Regresión** | Modelo para describir o estimar relaciones entre variables. | Estimar tiempo de respuesta según carga. |
| **Guardrail experimental** | Métrica vigilada para detectar daños colaterales del cambio. | Suben conversiones pero también reclamaciones. |
| **pandas / NumPy** | Librerías Python para manipular datos tabulares / cálculo numérico. | DataFrame de reservas; vectores numéricos. |
| **Matplotlib / Plotly** | Librerías de gráficos estáticos/interactivos. | Evolución temporal y dashboard exploratorio. |
| **Streamlit** | Herramienta Python para crear aplicaciones de datos. | App para explorar KPIs por segmento. |

## 9. IA aplicada, seguridad y proyecto (M5/M6/M7/M10)

| Término | Definición | Ejemplo |
|---|---|---|
| **IA generativa (GenAI)** | Modelos capaces de generar texto, código u otros contenidos. | Proponer una consulta SQL que hay que revisar. |
| **Prompt** | Instrucción y contexto proporcionados a un modelo de IA. | Pedir validación de un KPI con fórmula y datos de ejemplo. |
| **Alucinación** | Respuesta plausible pero no sustentada o incorrecta de una IA. | Citar una fuente inexistente. |
| **Verificación humana** | Contrastar salidas de herramientas con evidencia independiente. | Revisar cálculo, fuente y supuestos. |
| **Dato personal** | Información sobre una persona física identificada o identificable. | Nombre con identificador de usuario. |
| **Anonimización / seudonimización** | Transformación irreversible que impide identificar personas / sustitución de identificadores con posibilidad de reidentificación usando información adicional. | No son equivalentes jurídicamente. |
| **Datos sintéticos** | Datos generados artificialmente para ensayar métodos; no son necesariamente anónimos por el mero hecho de llamarse sintéticos. | Simular reservas sin usar datos personales reales. |
| **Cloud / on-premises** | Procesamiento alojado por un proveedor externo / infraestructura bajo control de la organización. | Colab frente a servidor interno. |
| **Control de acceso** | Reglas que determinan quién puede consultar o modificar datos. | Acceso restringido a información sensible. |
| **Ética de datos** | Evaluación responsable de utilidad, privacidad, equidad y posibles daños. | Evitar inferencias injustas sobre participantes. |
| **Revisión de código (code review)** | Comprobación estructurada de cambios por otra persona. | PR con observaciones y correcciones. |
| **MVP (Minimum Viable Product)** | Versión mínima útil para validar una necesidad o hipótesis. | Dashboard con los tres indicadores principales. |
| **Sprint** | Periodo acotado de trabajo orientado a un entregable. | Entregar una versión funcional en una semana. |
| **Demo Day** | Presentación de resultados y defensa de decisiones. | Mostrar evidencia, límites y recomendación final. |

---

# PARTE III — Fichas de uso y autoevaluación

## 10. Plantilla para definir correctamente una métrica

Al crear un KPI, completar **todos** los campos:

| Campo | Pregunta a responder |
|---|---|
| Nombre | ¿Cómo se llama? |
| Objetivo | ¿Qué decisión de negocio apoya? |
| Definición operativa | ¿Qué se incluye y excluye? |
| Fórmula | ¿Cuál es el numerador, denominador y unidad? |
| Grano y unidad de análisis | ¿Reserva, persona, curso, sesión? |
| Ventana temporal | ¿Día, semana, mes, cohortes desde alta? |
| Fuente y fiabilidad | ¿De dónde provienen los datos y qué limitaciones tienen? |
| Segmentos | ¿Por canal, fecha, servicio, ubicación? |
| Baseline y target | ¿Cuál es el punto de partida y la meta? |
| Responsable | ¿Quién interpreta y actúa si la métrica cambia? |
| Guardrail | ¿Qué daño lateral debe evitarse? |

### Ejemplo resuelto de KPI

**Nombre:** tasa semanal de finalización de reservas.

**Definición:** reservas únicas iniciadas durante la semana W que alcanzan estado «confirmada» dentro de 24 horas, dividido por reservas únicas iniciadas durante W. Los intentos cancelados o no completados permanecen en el denominador. Se excluyen registros duplicados de la misma reserva.

**Fórmula:**

`100 × reservas iniciadas en W y confirmadas ≤24 h / reservas iniciadas en W`

**Ejemplo didáctico:** 72 confirmadas dentro de 24 horas entre 120 iniciadas = **60 %**. La semana anterior fueron 60 de 120 = **50 %**. El cambio es de **+10 puntos porcentuales** y **+20 % relativo**.

**Guardrail:** tasa de incidencias / reservas completadas. **Limitación:** una reserva confirmada no demuestra que se haya disfrutado la actividad.

## 11. Diferencias que conviene dominar

| No confundir | Diferencia esencial |
|---|---|
| Dato vs. métrica | Un registro aislado no es un resumen cuantitativo definido. |
| Métrica vs. KPI | No toda medida está vinculada a un objetivo estratégico prioritario. |
| KPI vs. North Star | Una NSM busca representar valor central del producto; los KPIs pueden servir a distintos objetivos. |
| Resultado (`outcome`) vs. actividad (`output`) | Realizar un taller no demuestra mejorar empleabilidad. |
| Conversión vs. retención | Completar una acción ahora no es lo mismo que regresar a lo largo del tiempo. |
| Puntos porcentuales vs. porcentaje relativo | Del 50 % al 55 % = +5 pp = +10 % relativo. |
| Usuario vs. reserva | Una persona puede generar varias reservas; afectan al grano y al denominador. |
| `None` / nulo vs. cero | «No se sabe/no aplica» no es «cantidad nula medida». |
| Correlación vs. causalidad | Moverse juntos no demuestra que uno cause al otro. |
| Git vs. GitHub | Git gestiona versiones; GitHub aloja repositorios y facilita colaboración. |
| `commit` vs. `push` | Un commit guarda cambios en el historial local; push los envía al remoto. |
| CI vs. CD | Validar cambios no es lo mismo que entregar/desplegar resultados. |
| Datos anonimizados vs. seudonimizados | Con posibilidad de reidentificación, siguen siendo datos personales. |

---

