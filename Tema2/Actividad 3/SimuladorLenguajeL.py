# SIMULADOR DE ANÁLISIS SEMÁNTICO - LENGUAJE L
# Escenario Operativo B: Balance de Carga y Optimización Autónoma
# Desarrollado por: Genesis Moya C.I 31.370.339

# --- DEFINICIÓN LÉXICA (Constantes) ---
CONECTADO = True
AISLADO = False

# --- ACTUADORES SIMULADOS ---
def conmutar_linea(sector, estado):
    accion = "CONECTADO" if estado else "AISLADO"
    print(f"[ACCION SINTACTICA] Rele '{sector}' ha sido {accion}")

def inyectar_red(estado):
    if estado:
        print("[ACCION SINTACTICA] Inyectando excedente a la red publica")

# --- 1. LECTURA DE SENSORES ---
print("\n=== LECTURA DE SENSORES ECO-GRID ===")
nivel_bateria = float(input("Ingrese el nivel de bateria de 'banco_litio_1' (0-100%): "))
generacion_actual = float(input("Ingrese la generacion de 'inversor_paneles_solares' (kW): "))
demanda_actual = float(input("Ingrese la demanda de 'inversor_consumo_planta' (kW): "))

print("\n=== EVALUANDO ARBOL DE SINTAXIS (AST) ===")

# --- 2. EVALUACIÓN LÓGICA Y TOMA DE DECISIONES ---

# Caso A: Batería óptima y generación excede demanda
if (nivel_bateria > 90) and (generacion_actual > demanda_actual):
    print("-> FLUJO DE CONTROL: Caso A (Excedente de energia)")
    conmutar_linea("rele_red_publica", CONECTADO)
    inyectar_red(CONECTADO)

# Caso B: Batería en límite crítico y sin generación solar (Emergencia nocturna)
elif (nivel_bateria < 20) and (generacion_actual == 0):
    print("-> FLUJO DE CONTROL: Caso B (Emergencia nocturna)")
    conmutar_linea("rele_linea_produccion", AISLADO)
    conmutar_linea("rele_oficinas_administrativas", AISLADO)
    
    conmutar_linea("rele_area_medica", CONECTADO)
    conmutar_linea("rele_servidores_criticos", CONECTADO)

else:
    print("-> FLUJO DE CONTROL: Estado intermedio. No se requieren acciones críticas.")
print("===========================================\n")