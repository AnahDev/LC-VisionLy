import math
import time

def calcular_cuadratica_vectores():
    n = 200
    # Inicialización homogénea de vectores (datos estables)
    a = [2.0] * n
    b = [5.0] * n
    c = [2.0] * n
    x = [0.0] * n

    iteraciones = 100000
    
    start_time = time.perf_counter()
    
    for _ in range(iteraciones):
        for i in range(n):
            discriminante = b[i]**2 - 4 * a[i] * c[i]
            x[i] = (-b[i] + math.sqrt(discriminante)) / (2 * a[i])
            
    end_time = time.perf_counter()
    
    tiempo_ms = (end_time - start_time) * 1000
    print(f"Tiempo de ejecución (Python): {tiempo_ms:.2f} ms")

if __name__ == "__main__":
    calcular_cuadratica_vectores()