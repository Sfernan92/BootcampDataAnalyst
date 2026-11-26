📚 GUÍA COMPLETA DE GIT
Chuleta de comandos para proyectos de Data Analyst

Guía de consulta rápida para trabajar con Git, controlar versiones, gestionar ramas y subir proyectos a GitHub.

📌 ÍNDICE
🔍 Consultar el estado del proyecto
📝 Ver las modificaciones
📦 Preparar y deshacer cambios
💾 Guardar cambios (commit)
📜 Consultar el historial
🌿 Trabajar con ramas (branches)
🔀 Fusionar ramas (merge)
☁️ Subir cambios a GitHub (push)
🧠 Flujo completo de trabajo
⚠️ Comandos que debemos utilizar con cuidado
🎯 Resumen rápido de comandos
1. 🔍 CONSULTAR EL ESTADO DEL PROYECTO
git status

¿Para qué sirve?

Muestra el estado actual de los archivos del proyecto.

Permite saber:

Qué archivos han sido modificados.
Qué archivos son nuevos.
Qué archivos están preparados para el commit.
Qué cambios todavía no están preparados.

Ejemplo:

bash
git status


💡 Recuerda: Es como una fotografía del estado actual de tu proyecto.

2. 📝 VER LAS MODIFICACIONES
git diff

¿Para qué sirve?

Muestra las diferencias exactas dentro de los archivos modificados que todavía no has preparado con git add.

bash
git diff


¿Qué significan los símbolos?

🔴 - Línea eliminada o sustituida.
🟢 + Línea añadida.
Sin símbolo: línea que permanece igual.
git diff --staged

¿Para qué sirve?

Muestra las modificaciones que ya has preparado con git add y que todavía no has guardado en un commit.

bash
git diff --staged

git diff HEAD

¿Para qué sirve?

Muestra todas las diferencias respecto al último commit, tanto las preparadas como las que todavía no lo están.

bash
git diff HEAD

git diff HEAD~1 HEAD -- analisis.py

¿Para qué sirve?

Compara el archivo analisis.py entre el commit anterior y el commit actual.

bash
git diff HEAD~1 HEAD -- analisis.py

git diff HEAD~2 HEAD -- analisis.py

Compara analisis.py entre el commit de hace dos posiciones y el commit actual.

bash
git diff HEAD~2 HEAD -- analisis.py


Conceptos importantes:

HEAD: commit actual.
HEAD~1: commit anterior.
HEAD~2: dos commits anteriores.
--: separa las referencias de los commits de la ruta del archivo.

💡 Recuerda:

git status = ¿Qué archivos he modificado?
git diff = ¿Qué he cambiado dentro de ellos?
3. 📦 PREPARAR Y DESHACER CAMBIOS
git add README.md

¿Para qué sirve?

Prepara los cambios de un archivo concreto para el próximo commit.

bash
git add README.md

git add .

¿Para qué sirve?

Prepara los cambios de todos los archivos del directorio actual y sus subdirectorios.

bash
git add .

git restore --staged README.md

¿Para qué sirve?

Saca el archivo del área de preparación (Staging Area), pero mantiene las modificaciones en el archivo.

bash
git restore --staged README.md


⚠️ No elimina los cambios. Simplemente deshace el git add.

git restore README.md

¿Para qué sirve?

Descarta las modificaciones no preparadas de ese archivo y recupera su versión del área de preparación o, si no hay cambios preparados, del último commit.

bash
git restore README.md


⚠️ ¡Cuidado! Puedes perder modificaciones que no hayas guardado en un commit.

4. 💾 GUARDAR CAMBIOS (COMMIT)
git commit -m "mensaje"

¿Para qué sirve?

Guarda los cambios preparados en un nuevo commit dentro del historial local de Git.

bash
git commit -m "Actualizo README"


Otros ejemplos:

bash
git commit -m "Limpieza de datos"
git commit -m "Añado gráficos"
git commit -m "Corrijo errores del análisis"


📌 Importante:

Un commit es una versión registrada de tu proyecto.

El comando git commit guarda los cambios en el repositorio local, pero todavía no los sube a GitHub.

5. 📜 CONSULTAR EL HISTORIAL
git log

¿Para qué sirve?

Muestra el historial de commits realizados en el proyecto.

bash
git log

git log --oneline

Muestra los commits resumidos en una sola línea.

bash
git log --oneline

git log --oneline --graph --decorate -5

Muestra los últimos cinco commits de forma visual.

bash
git log --oneline --graph --decorate -5


Significado:

--oneline: un commit por línea.
--graph: representa gráficamente las ramas.
--decorate: muestra referencias como HEAD, main y etiquetas.
-5: muestra los últimos cinco commits.
git show --stat HEAD

¿Para qué sirve?

Muestra un resumen del último commit y los archivos que se modificaron.

bash
git show --stat HEAD


Permite conocer:

Número de archivos modificados.
Líneas añadidas.
Líneas eliminadas.
git show HEAD

Muestra información detallada del último commit, incluyendo las modificaciones línea por línea.

bash
git show HEAD


💡 Recuerda:

git log = historial de commits.
git show --stat HEAD = resumen del último commit.
git show HEAD = detalles de los cambios del último commit.
6. 🌿 TRABAJAR CON RAMAS (BRANCHES)

¿Qué es una rama?

Una rama es una línea de trabajo independiente que permite desarrollar mejoras sin modificar directamente la rama principal (main).

Por ejemplo, podemos crear una rama para mejorar el análisis de visitas.

git branch

Muestra las ramas locales existentes.

bash
git branch


El símbolo * indica la rama en la que estamos trabajando actualmente.

git branch mejora/descripcion

Crea una rama nueva, pero NO cambia a ella.

bash
git branch mejora/descripcion

git switch mejora/descripcion

Cambia a una rama que ya existe.

bash
git switch mejora/descripcion

git switch main

Vuelve a la rama principal.

bash
git switch main

git switch -c mejora/descripcion

Crea una rama nueva y cambia automáticamente a ella.

bash
git switch -c mejora/descripcion


Diferencia entre los comandos:

Comando	Función
git branch nombre	Crea una rama.
git switch nombre	Cambia de rama.
git switch -c nombre	Crea y cambia de rama.

💡 Consejo: Utiliza nombres descriptivos para tus ramas.

Ejemplos:

bash
git branch mejora/graficos
git branch mejora/limpieza-datos
git branch correccion/errores

7. 🔀 FUSIONAR RAMAS (MERGE)
git merge mejora/descripcion

¿Para qué sirve?

Incorpora los cambios de una rama dentro de la rama en la que estamos situados.

Ejemplo: queremos incorporar las mejoras de mejora/descripcion a main.

PASO 1. Cambiamos a la rama principal.

bash
git switch main


PASO 2. Fusionamos la rama de mejora.

bash
git merge mejora/descripcion


PASO 3. Comprobamos el historial.

bash
git log --oneline --graph --decorate -5


📌 MUY IMPORTANTE:

El merge se ejecuta desde la rama que va a recibir los cambios.

En nuestro ejemplo:

Rama que recibe los cambios: main.
Rama que aporta los cambios: mejora/descripcion.

⚠️ Recuerda escribir exactamente el nombre de la rama.

8. ☁️ SUBIR CAMBIOS A GITHUB (PUSH)
git push

¿Para qué sirve?

Envía los commits locales a la rama remota correspondiente del repositorio.

bash
git push


Flujo habitual:

bash
git add .
git commit -m "Actualizo proyecto"
git push


📌 IMPORTANTE:

Git no sube directamente los archivos modificados con git push.

Sube los commits que hayas creado.

Por tanto:

git add = prepara los cambios.
git commit = registra los cambios.
git push = sube los commits al repositorio remoto.

Si has creado una rama nueva y quieres publicarla por primera vez:

bash
git push -u origin mejora/descripcion

9. 🧠 FLUJO COMPLETO DE TRABAJO

Este es el proceso habitual para trabajar en un proyecto de análisis de datos.

PASO 1. Comprobar el estado
bash
git status

PASO 2. Revisar las modificaciones
bash
git diff

PASO 3. Preparar los cambios
bash
git add .

PASO 4. Revisar los cambios preparados
bash
git diff --staged

PASO 5. Crear el commit
bash
git commit -m "Actualizo el análisis"

PASO 6. Consultar el historial
bash
git log --oneline --graph --decorate -5

PASO 7. Subir los cambios
bash
git push

10. 🌳 FLUJO COMPLETO CON RAMAS

Ejemplo práctico: queremos mejorar los gráficos de nuestro proyecto de visitas.

1. Crear una rama nueva.

bash
git branch mejora/graficos


2. Cambiar a ella.

bash
git switch mejora/graficos


3. Modificar los archivos.

Trabajamos en nuestro archivo analisis.py.

4. Preparar los cambios.

bash
git add .


5. Crear un commit.

bash
git commit -m "Añado nuevos gráficos"


6. Volver a main.

bash
git switch main


7. Fusionar las mejoras.

bash
git merge mejora/graficos


8. Subir los cambios.

bash
git push

11. ⚠️ COMANDOS QUE DEBES UTILIZAR CON CUIDADO
Comando	Precaución
git restore archivo	Puede descartar modificaciones no preparadas.
git restore --staged archivo	Quita los cambios del staging, pero los conserva en el archivo.
git branch -d rama	Elimina una rama local.
git merge rama	Puede generar conflictos si hay cambios incompatibles.
12. 🎯 RESUMEN RÁPIDO: TODOS LOS COMANDOS
Necesidad	Comando
Consultar estado	git status
Ver cambios	git diff
Ver cambios preparados	git diff --staged
Comparar con HEAD	git diff HEAD
Comparar commits	git diff HEAD~1 HEAD
Añadir archivo	git add archivo
Añadir todos los cambios	git add .
Quitar del staging	git restore --staged archivo
Descartar modificaciones	git restore archivo
Crear commit	git commit -m "mensaje"
Ver historial	git log
Historial resumido	git log --oneline
Historial gráfico	git log --oneline --graph --decorate -5
Ver resumen del último commit	git show --stat HEAD
Ver detalles del último commit	git show HEAD
Ver ramas	git branch
Crear rama	git branch nombre
Cambiar de rama	git switch nombre
Crear y cambiar de rama	git switch -c nombre
Fusionar ramas	git merge nombre
Subir commits	git push
💡 CONSEJO FINAL

Para aprender Git, intenta recordar esta secuencia:

MODIFICAR → REVISAR → PREPARAR → GUARDAR → SUBIR

bash
git status
git diff
git add .
git diff --staged
git commit -m "Descripción del cambio"
git push


🚀 ¡Con estos comandos tienes una base sólida para gestionar tus proyectos de Data Analyst con Git y GitHub!