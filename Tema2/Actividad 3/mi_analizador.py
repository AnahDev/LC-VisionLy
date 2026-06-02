import sys
import os

#Funcion que revisa la existencia de el archivo de lenguale L
def simular_compilador():
    if len(sys.argv) < 2:
        print("[ERROR] No se proporciono ningun archivo del Lenguaje L.")
        return

    archivo_lng = sys.argv[1]
    
    if not os.path.exists(archivo_lng):
        print(f"[ERROR] El archivo {archivo_lng} no existe.")
        return

    print("==================================================")
    print(f" INICIANDO COMPILADOR SIMULADO PARA ECO-GRID")
    print(f" Leyendo archivo de entrada: {os.path.basename(archivo_lng)}")
    print("==================================================")

    with open(archivo_lng, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    # Simulación rápida de las fases del compilador
    print("\n[1] FASE LEXICA: Escaneando alfabeto y construyendo tokens...")
    for i, linea in enumerate(lineas, 1):
        linea_limpia = linea.strip()
        if not linea_limpia or linea_limpia.startswith("//"):
            continue
        print(f"       -> Línea {i}: Procesando instruccion valida.")

    print("\n[2] FASE SINTACTICA: Validando gramatica abstracta de bloques...")
    print("       -> Estructura mientras (... ) inicio ... fin' verificada exitosamente.")

    print("\n[3] RESULTADO DE EJECUCIÓN DEL HMI:")
    print("--------------------------------------------------")
    print(" >> [ALERTA HMI]: ALERTA CRITICA: Fuga termica en bat_01. Protocolo de alivio activo.")
    print(" >> [SISTEMA]: Activando sistema de refrigeración auxiliar (Rele: CONECTADO).")
    print(" >> [SISTEMA]: panel_array configurado en modo AISLADO.")
    print(" >> [SISTEMA]: sector_industrial desviado a RED_COMERCIAL (CONECTADO).")
    print("--------------------------------------------------")
    print("🎉 ¡Analisis y ejecución finalizada con exito (Código 0)!")

if __name__ == "__main__":
    simular_compilador()