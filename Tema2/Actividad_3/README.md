# ECO-GRID - Sistema de Gestion de Microredes Inteligentes

Este repositorio contiene el desarrollo de la actividad 3 del Tema 2

## Integrantes
* **Estudiante:** Carlos Martínez - Control de Planta y Gestion de Emergencias.
* **Estudiante:** Genesis Moya - Gestion de almacenamiento y Comercializacion.
* **Eslogan del Grupo:** "Mantenlo Simple"

##  ¿Como ejecutar los scripts del Lenguaje L (Actividad III)?

Hemos diseñado un DSL conceptual adaptado a operadores del sistema físico simulado de la planta ECO-GRID

### Pasos para ejecutar el analizador en VS Code:
#### Para el Escenario A
1. Abra la carpeta raíz de este proyecto (`Actividad 3`) en **Visual Studio Code**.
2. Asegúrese de que el archivo del script del compilador (`mi_analizador.py`) esté en la misma ruta.
3. Abra el archivo de codigo correspondiente al escenario que desea evaluar (`escenario_a.lng`).
4. Con la pestaña del escenario activa en su pantalla, presione la combinación de teclas **`Ctrl + Shift + B o ejecute en la terminal: python mi_analizador.py escenario_a.lng`**.
5. La terminal integrada de VS Code ejecutará de forma automática el análisis léxico y sintáctico del programa, imprimiendo las alertas correspondientes en la interfaz HMI.

#### Para el Escenario B 
1. Abra la carpeta raíz de este proyecto (`Actividad 3`) en **Visual Studio Code**.
2. Asegúrese de que el archivo del intérprete semántico (`SimuladorLenguajeL.py`) y el archivo de texto con el código del lenguaje (`Escenario_B.txt`) se encuentren en la misma ruta.
3. Abra la terminal integrada de VS Code y ejecute el siguiente comando:
   **`python SimuladorLenguajeL.py`**
4. El programa iniciará el simulador semántico interactivo de la microred. La consola le solicitará que ingrese los valores de los sensores (ej. nivel de batería al 15%, generación solar en 0 y el consumo de planta 150) para realizar una prueba de escritorio dinámica.
5. El flujo de control evaluará el Árbol de Sintaxis Abstracta (AST) e imprimirá en consola las decisiones de conmutación de los relés demostrando la coherencia lógica del Lenguaje L.
