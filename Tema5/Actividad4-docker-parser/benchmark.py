import os
import subprocess
import time

def run_benchmark():
    # Compilar C
    print(" Compilando parser en C...")
    compile_res = subprocess.run(["gcc", "parser_c.c", "-o", "parser_c"])
    if compile_res.returncode != 0:
        print(" Error compilando C")
        return

    # Obtener archivos ordenados
    files = sorted(
        [f for f in os.listdir("dataset") if f.endswith(".yml")], 
        key=lambda x: int(x.split('-')[2].split('.')[0])
    )

    print(" Iniciando experimento de carga entre lenguajes...\n")
    
    # Encabezado para la consola y archivo CSV
    csv_lines = ["Archivo,C_ms,NodeJS_ms,Python_ms\n"]
    print(f"{'Archivo':<20} | {'C (ms)':<10} | {'Node.js (ms)':<12} | {'Python (ms)':<10}")
    print("-" * 60)

    for f in files:
        filepath = os.path.join("dataset", f)

        # Medir C (Compilado)
        t0 = time.perf_counter()
        subprocess.run(["./parser_c", filepath], stdout=subprocess.DEVNULL)
        t1 = time.perf_counter()
        time_c = (t1 - t0) * 1000

        # Medir Node.js (Motor JIT)
        t0 = time.perf_counter()
        subprocess.run(["node", "parser_js.js", filepath], stdout=subprocess.DEVNULL)
        t1 = time.perf_counter()
        time_js = (t1 - t0) * 1000

        # Medir Python (Interpretado)
        t0 = time.perf_counter()
        subprocess.run(["python3", "parser_python.py", filepath], stdout=subprocess.DEVNULL)
        t1 = time.perf_counter()
        time_py = (t1 - t0) * 1000

        # Mostrar en consola
        print(f"{f:<20} | {time_c:<10.3f} | {time_js:<12.3f} | {time_py:<10.3f}")
        
        # Guardar linea CSV
        csv_lines.append(f"{f},{time_c:.3f},{time_js:.3f},{time_py:.3f}\n")

    # Guardar resultados en archivo
    with open("tiempos.csv", "w") as out:
        out.writelines(csv_lines)

    print("\n Experimento finalizado con éxito.")
    print(" Tiempos guardados correctamente en 'tiempos.csv'.")

if __name__ == "__main__":
    run_benchmark()