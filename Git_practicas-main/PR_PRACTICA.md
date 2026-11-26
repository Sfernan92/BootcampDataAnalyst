# Guion de la práctica: colaboración en GitHub

## Antes de empezar

- Cuenta GitHub operativa y Git Bash/VS Code instalados.
- Un repositorio propio de prueba o permisos en el repositorio del equipo.
- La carpeta `proyecto_visitas`, sin datos reales.
- En grupos de 3–4, elegid: autor/a, revisor/a y verificador/a; rotad después.

## Microprácticas (con evidencia)

| ID | Trabajo | Evidencia |
|---|---|---|
| P1 | `git init -b main` y `git status` | Pantalla de rama y archivos sin rastrear |
| P2 | Primer commit | `git log --oneline` |
| P3 | Preparar un solo archivo | `git status` muestra staging selectivo |
| P4 | `git diff --staged`, `git restore --staged` | Edición sigue visible sin quedar preparada |
| P5 | Identificar commit | Hash abreviado y `git show --stat` |
| P6 | Rama de mejora | `git branch --show-current` y comparación con main |
| P7 | Publicar remoto | Enlace a GitHub y ficheros visibles |
| P8 | Clonar en carpeta separada | Carpeta clonada con historial |
| P9 | Abrir PR | URL de PR con resumen del cambio |
| P10 | Revisar y fusionar | Comentario específico y decisión |
| P11 | Diagnosticar conflicto | Decisión sobre línea incompatible |
| P12 | Distinguir deshacer | Explicación restore-staged / restore / revert |

## Criterios de aceptación

- README explica qué es la tasa de conversión, su fórmula y cómo ejecutar el script.
- Los datos del repositorio son inventados y no incluyen información privada.
- Cada commit tiene un mensaje descriptivo; la PR se comprende sin preguntar al autor.
- Una segunda persona revisa o comenta antes del merge.

## Escalado si algo falla

1. Ejecuta `git status` y lee el error literal.
2. Comprueba ruta del proyecto (`pwd`), rama (`git branch --show-current`) y remoto (`git remote -v`).
3. Pide a tu pareja que contraste el estado antes de usar comandos destructivos.
4. Si el bloqueo es autenticación, usa GitHub Desktop y conserva la evidencia del cambio.

## Ampliación

Copia `.github/workflows/calidad.yml` desde `ampliacion/` en la raíz del proyecto.
Entra en **Actions** y registra si la ejecución pasa, cuál fue su trigger y qué comprobó.
