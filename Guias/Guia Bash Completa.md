
<!-- ================================================== -->
<!--          GUÍA VISUAL DE GIT BASH                   -->
<!-- ================================================== -->

<div align="center">

# ⚡ GIT BASH

### GUÍA PRÁCTICA DE COMANDOS ESENCIALES

**CREAR · EDITAR · MODIFICAR · ORGANIZAR**

---

📁 Archivos & Carpetas · 💻 Terminal · 🔧 Git

**Nivel:** Principiante  
**Entorno:** Windows · Git Bash · Visual Studio Code

</div>

---

# 📚 ÍNDICE

| Nº | Sección | Contenido |
|:--:|---|---|
| 01 | Navegación | Desplazarse por directorios |
| 02 | Carpetas | Crear directorios |
| 03 | Archivos | Crear archivos |
| 04 | Lectura | Consultar contenido |
| 05 | Edición | Modificar archivos |
| 06 | Contenido | Añadir y reemplazar texto |
| 07 | Organización | Copiar, mover y renombrar |
| 08 | Eliminación | Borrar archivos y carpetas |
| 09 | Búsqueda | Buscar archivos y texto |
| 10 | Git | Gestionar cambios |
| 11 | Práctica | Crear un proyecto |
| 12 | Chuleta | Comandos principales |

---

# 01 · NAVEGACIÓN POR DIRECTORIOS

Comandos para desplazarnos por las carpetas de nuestro ordenador.

### 📍 Consultar ubicación actual

```bash
pwd
```

Muestra la ruta del directorio en el que estamos.

### 📂 Mostrar archivos y carpetas

```bash
ls
```

Muestra los elementos del directorio actual.

```bash
ls -a
```

Muestra también los archivos ocultos.

```bash
ls -la
```

Muestra todos los elementos con información adicional.

### ➡️ Entrar en una carpeta

```bash
cd nombre_carpeta
```

### ⬅️ Retroceder una carpeta

```bash
cd ..
```

### 🏠 Ir al directorio personal

```bash
cd ~
```

### 🧹 Limpiar la terminal

```bash
clear
```

> **Consejo:** utiliza `pwd` y `ls` constantemente para saber dónde estás y qué archivos tienes.

---

# 02 · CREACIÓN DE CARPETAS

Los directorios permiten organizar nuestros proyectos y archivos.

### Crear una carpeta

```bash
mkdir proyectos
```

### Crear varias carpetas

```bash
mkdir carpeta1 carpeta2 carpeta3
```

### Crear carpetas anidadas

```bash
mkdir -p proyecto/src/css
```

**Resultado:**

```text
proyecto/
└── src/
    └── css/
```

---

# 03 · CREACIÓN DE ARCHIVOS

Podemos crear archivos vacíos o archivos que ya contengan texto.

### Crear un archivo vacío

```bash
touch archivo.txt
```

### Crear un archivo Markdown

```bash
touch README.md
```

### Crear varios archivos

```bash
touch index.html estilos.css script.js
```

### Crear un archivo con contenido

```bash
echo "Hola mundo" > archivo.txt
```

**Resultado:**

```text
archivo.txt
└── Hola mundo
```

### Crear un archivo escribiendo varias líneas

```bash
cat > archivo.md
```

Escribe el contenido y pulsa `Ctrl + D` para finalizar.

---

# 04 · LECTURA DE ARCHIVOS

Comandos para consultar el contenido de los archivos.

### Mostrar todo el contenido

```bash
cat README.md
```

### Leer archivos largos

```bash
less README.md
```

Pulsa `q` para salir.

### Mostrar las primeras líneas

```bash
head README.md
```

### Mostrar las últimas líneas

```bash
tail README.md
```

### Consultar cambios en tiempo real

```bash
tail -f archivo.log
```

Pulsa `Ctrl + C` para salir.

---

# 05 · EDICIÓN DE ARCHIVOS

Podemos editar archivos desde la terminal o mediante un editor externo.

### ✏️ Nano

```bash
nano archivo.txt
```

| Atajo | Función |
|---|---|
| `Ctrl + O` | Guardar |
| `Enter` | Confirmar |
| `Ctrl + X` | Salir |
| `Ctrl + K` | Cortar línea |
| `Ctrl + U` | Pegar línea cortada |

### 💻 Visual Studio Code

Abrir un archivo:

```bash
code archivo.txt
```

Abrir el proyecto completo:

```bash
code .
```

### 📝 Bloc de notas de Windows

```bash
notepad archivo.txt
```

> **Recomendación:** utiliza `code .` cuando trabajes con proyectos de programación. Te permitirá gestionar todos los archivos desde VS Code.

---

# 06 · AÑADIR Y MODIFICAR CONTENIDO

Hay dos operadores fundamentales para escribir en archivos: `>` y `>>`.

### Sobrescribir contenido

```bash
echo "Nuevo contenido" > archivo.txt
```

El operador `>` reemplaza todo el contenido anterior.

### Añadir contenido al final

```bash
echo "Nueva línea" >> archivo.txt
```

El operador `>>` conserva el contenido anterior y añade texto al final.

### Añadir varias líneas

```bash
cat >> archivo.txt
```

Escribe las líneas y pulsa `Ctrl + D` para terminar.

### Reemplazar palabras

```bash
sed -i 's/hola/adios/g' archivo.txt
```

Reemplaza todas las apariciones de `hola` por `adios`.

### Diferencias entre operadores

| Operador | Función |
|:---:|---|
| `>` | Sobrescribir contenido |
| `>>` | Añadir contenido |
| `<` | Redirigir entrada |

> ⚠️ **Importante:** ten cuidado con `>`, porque puedes borrar accidentalmente el contenido anterior de un archivo.

---

# 07 · COPIAR, MOVER Y RENOMBRAR

### Copiar un archivo

```bash
cp archivo.txt copia.txt
```

### Copiar un archivo a otra carpeta

```bash
cp archivo.txt carpeta/
```

### Copiar una carpeta completa

```bash
cp -r carpeta1 carpeta2
```

### Mover un archivo

```bash
mv archivo.txt carpeta/
```

### Renombrar un archivo

```bash
mv antiguo.txt nuevo.txt
```

### Renombrar una carpeta

```bash
mv carpeta_antigua carpeta_nueva
```

---

# 08 · ELIMINAR ARCHIVOS Y CARPETAS

⚠️ **ATENCIÓN:** los comandos de eliminación normalmente no envían los elementos a la papelera de reciclaje.

### Eliminar un archivo

```bash
rm archivo.txt
```

### Eliminar varios archivos

```bash
rm archivo1.txt archivo2.txt
```

### Eliminar una carpeta vacía

```bash
rmdir carpeta
```

### Eliminar una carpeta con todo su contenido

```bash
rm -r carpeta
```

> Comprueba siempre la ruta y el contenido antes de ejecutar un comando de eliminación.

---

# 09 · BUSCAR ARCHIVOS Y TEXTO

### Buscar un archivo por nombre

```bash
find . -name "archivo.txt"
```

### Buscar archivos Markdown

```bash
find . -name "*.md"
```

### Buscar una palabra dentro de un archivo

```bash
grep "palabra" archivo.txt
```

### Buscar una palabra en toda una carpeta

```bash
grep -r "palabra" .
```

---

# 10 · COMANDOS BÁSICOS DE GIT

Git permite controlar las modificaciones realizadas en nuestro proyecto.

### Consultar el estado

```bash
git status
```

### Ver las modificaciones

```bash
git diff
```

### Añadir un archivo al área de preparación

```bash
git add archivo.txt
```

### Añadir todos los cambios

```bash
git add .
```

### Crear un commit

```bash
git commit -m "Primer commit"
```

### Consultar el historial

```bash
git log
```

---

# 11 · EJERCICIO PRÁCTICO

## 🚀 Crear nuestro primer proyecto

Vamos a crear una estructura sencilla utilizando únicamente Git Bash.

### PASO 01 · Crear el directorio

```bash
mkdir mi_proyecto
```

### PASO 02 · Entrar en el directorio

```bash
cd mi_proyecto
```

### PASO 03 · Crear los archivos

```bash
touch README.md index.html estilos.css
```

### PASO 04 · Crear una carpeta de imágenes

```bash
mkdir img
```

### PASO 05 · Escribir contenido en README

```bash
echo "# Mi primer proyecto" > README.md
```

### PASO 06 · Abrir el proyecto en VS Code

```bash
code .
```

### PASO 07 · Comprobar el resultado

```bash
ls -la
```

### 📁 Estructura final

```text
mi_proyecto/
│
├── README.md
├── index.html
├── estilos.css
│
└── img/
```

**¡Enhorabuena!** Ya has creado tu primer proyecto utilizando Git Bash.

---

# 12 · CHULETA RÁPIDA

## ⭐ Comandos imprescindibles

| Comando | Función |
|---|---|
| `pwd` | Ver ubicación actual |
| `ls` | Listar archivos |
| `ls -a` | Mostrar ocultos |
| `cd carpeta` | Entrar en carpeta |
| `cd ..` | Retroceder |
| `mkdir` | Crear carpeta |
| `touch` | Crear archivo |
| `echo` | Mostrar o escribir texto |
| `cat` | Leer o escribir contenido |
| `less` | Leer archivos largos |
| `nano` | Editar archivos |
| `code .` | Abrir VS Code |
| `cp` | Copiar |
| `mv` | Mover o renombrar |
| `rm` | Eliminar |
| `rmdir` | Eliminar carpeta vacía |
| `find` | Buscar archivos |
| `grep` | Buscar texto |
| `clear` | Limpiar terminal |
| `git status` | Consultar estado de Git |
| `git add .` | Preparar cambios |
| `git commit` | Crear un commit |

---

# 🧠 CONSEJOS FINALES

- Utiliza `pwd` para comprobar dónde estás.
- Utiliza `ls` para ver el contenido de una carpeta.
- Utiliza `touch` para crear archivos vacíos.
- Utiliza `mkdir` para crear directorios.
- Utiliza `cat` para leer archivos.
- Utiliza `nano` o `code` para editarlos.
- Recuerda que `>` sobrescribe y `>>` añade contenido.
- Comprueba las rutas antes de utilizar `rm`.

---

<div align="center">

---

# ⚡ FIN DE LA GUÍA

### GIT BASH · COMMAND LINE BASICS

**Aprende · Practica · Domina la terminal**

*Documentación personal de comandos de Git Bash.*

</div>
