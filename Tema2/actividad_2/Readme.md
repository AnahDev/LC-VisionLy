# Actividad II: Benchmarking Multiparadigma (Resolución de Ecuación de Segundo Grado)

Este módulo contiene la implementación de un algoritmo cerrado de alta carga computacional diseñado para evaluar y comparar el rendimiento físico (tiempo de ejecución y consumo de memoria RAM) de cuatro entornos y paradigmas tecnológicos distintos: **Python**, **JavaScript (Node.js)**, **Rust** y **Zig**.

El experimento realiza la resolución secuencial de una ecuación de segundo grado sobre vectores dinámicos de tamaño N = 200, iterando el proceso un total de 100,000 veces de forma masiva.

##  Instrucciones de Ejecución y Medición

A continuación se detallan los comandos necesarios para replicar las pruebas en sistemas basados en **Linux** y sistemas **Windows**.

###  1. En sistemas Linux (Ubuntu, Debian, Linux Mint)

Para medir el tiempo de ejecución interno se usan las salidas estándar de cada script. Para capturar el consumo exacto de memoria física real (*Maximum Resident Set Size*), se antepone la herramienta de diagnóstico `/usr/bin/time -v`.

* **Python:**
    ```bash
    cd python
    /usr/bin/time -v python3 ecuacion.py

* **JavaScript (Node.js):**
    ```bash
    cd ../javascript
    /usr/bin/time -v node ecuacion.js

* **Rust:**
    ```bash
    cd ../rust
    # Nota: Requiere haber compilado previamente con 'cargo build --release'
    /usr/bin/time -v ./target/release/ecuacion_rust

* **Zig:**
    ```bash
    cd ../zig
# Compilación AOT y ejecución directa libre de caché local
    zig build-exe main.zig -O ReleaseFast --name ecuacion_zig_tmp
    /usr/bin/time -v ./ecuacion_zig_tmp
    rm ecuacion_zig_tmp.o

## En sistemas Windows (PowerShell)
comando nativo de PowerShell Measure-Command para auditar el tiempo global, y la API Get-Process para rastrear la memoria máxima asignada en el Working Set.
Asegúrate de estar parado dentro de la carpeta de cada lenguaje en la consola de PowerShell:

* **Python**
    ```PowerShell
    cd python
    # Medir tiempo global en Windows
    Measure-Command { python ecuacion.py }

* **Javascript**
    ```PowerShell
    cd ..\javascript
    Measure-Command { node ecuacion.js }

* **Rust:**
    ```PowerShell
    cd ..\rust
    cargo build --release
    # Ejecutar y cronometrar el binario compilado de Windows
    Measure-Command { .\target\release\ecuacion_rust.exe }

* **Zig:**
  ## Para probar Zig en Windows, puedes descargar el binario oficial para Windows x86_64, compilar el ejecutable nativo .exe y cronometrarlo:
    ```PowerShell
    cd ..\zig
    # Compilación óptima para Windows (Genera un archivo ejecutable .exe)
    zig build-exe main.zig -O ReleaseFast --name ecuacion_zig_win
    # Medir tiempo global del binario nativo
    Measure-Command { .\ecuacion_zig_win.exe }
    # Limpieza de archivo temporal .exe y .pdb residual
    Remove-Item ecuacion_zig_win.exe, ecuacion_zig_win.pdb -ErrorAction SilentlyContinue

## Si desea capturar de forma detallada los Megabytes consumidos en Windows en tiempo real, puede abrir una segunda pestaña de PowerShell mientras se ejecutan los scripts pesados y correr el comando:
Get-Process | Sort-Object WorkingSet -Descending | Select-Object Name, @{Name="RAM (MB)";Expression={($_.WorkingSet/1MB).ToString("F2")}} -First 10