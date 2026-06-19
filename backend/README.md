# Dart Analyzer - Backend

Analizador de código Dart desarrollado en Python para procesar algoritmos y generar reportes de análisis léxico, semántico y sintáctico.

## Configuración del Proyecto (VS Code Tasks)

Para facilitar la preparación del entorno de desarrollo, el proyecto incluye tareas configuradas de VS Code (`tasks.json`). Puedes ejecutarlas presionando `Ctrl + Shift + P` -> `Tasks: Run Task`:

1. **Initialize venv**: Inicializa un entorno virtual de Python (`venv`) compatible con tu sistema operativo (Windows, macOS o Linux).
2. **Install Dependencies**: Activa el entorno virtual e instala los paquetes necesarios listados en `requirements.txt`.

Una vez ejecutadas las dos tareas anteriores, el entorno virtual existirá en tu disco duro, pero debes indicarle a Visual Studio Code que lo utilice por defecto. Esto es **obligatorio** para que el depurador (`F5`), el autocompletado y el detector de errores reconozcan las librerías instaladas (como `ply`).

Sigue estos pasos:
1. Presiona `Ctrl + Shift + P` para abrir la paleta de comandos de VS Code.
2. Escribe y selecciona la opción **`Python: Select Interpreter`** (Seleccionar intérprete).
3. En la lista que aparece, busca la ruta que apunte a nuestro entorno virtual. Si no la ves a simple vista, selecciona "Enter interpreter path..." (Introducir ruta del intérprete), dale a "Find..." (Buscar) y navega hasta el ejecutable:
   * **En Windows:** Selecciona `backend\venv\Scripts\python.exe`
   * **En macOS/Linux:** Selecciona `backend/venv/bin/python`

> [!TIP]
> Solo necesitas realizar este paso la primera vez que configures el proyecto. Visual Studio Code guardará tu elección para futuras sesiones de forma automática.

---

## Depuración y Ejecución (Launch Configurations)

El proyecto cuenta con una configuración de depuración en VS Code (`launch.json`) llamada **"Dart Analyzer: Parse algorithm file name"** que admite la entrada de argumentos mediante un cuadro de diálogo al iniciar el debugger (`F5`).

Deberás ingresar dos argumentos separados por un espacio: `<número_integrante> <nombre_archivo>`

### Argumento 1: Integrante del equipo (Números del 0 al 2)
Asigna el autor del análisis según la siguiente tabla:
* **`0`**: `alexandernieves`
* **`1`**: `sofiaizaguirre`
* **`2`**: `robertcortez`

### Argumento 2: Nombre del archivo Dart
El nombre del archivo Dart alojado en la carpeta `algorithms/`.
> [!IMPORTANT]
> **Solo debes ingresar el nombre del archivo**, sin la extensión `.dart` y sin rutas de carpetas (por ejemplo: ingresa `main` para el archivo `algorithms/main.dart`).

*Ejemplo de entrada de argumentos:*
```text
0 main
```

---

## Carpeta de Logs

Cada vez que el script se ejecuta correctamente, genera un archivo de resultados en la carpeta `logs/` con el siguiente formato de nombre:
`lexico-{nombre_integrante}-{fecha}-{hora}.txt`

*Ejemplo de archivo generado:*
`lexico-alexandernieves-19-06-2026-00h15m11s.txt`

> [!WARNING]
> **Políticas de Versionamiento de Logs:**
> No se deben subir al repositorio de Git aquellos archivos de registro (`logs/`) que no sean oficiales o que correspondan a pruebas personales irrelevantes. Mantengamos la carpeta de historial limpia.
