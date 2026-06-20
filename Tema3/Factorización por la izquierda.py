from collections import defaultdict

def factorizar_izquierda(no_terminal, producciones):
    """
    Toma un No-Terminal y sus producciones, y aplica factorización 
    por la izquierda agrupando automáticamente las reglas conflictivas.
    """
    # 1. Agrupar las producciones por su primer token (palabra)
    grupos = defaultdict(list)
    for prod in producciones:
        tokens = prod.split()
        if tokens:
            grupos[tokens[0]].append(tokens)
            
    nuevas_reglas_base = []
    nuevas_reglas_prima = []
    nuevo_nt = f"{no_terminal}'"
    
    # 2. Analizar cada grupo de producciones
    for primer_token, lista_tokens in grupos.items():
        # Si un grupo tiene más de 1 producción, hay conflicto (prefijo común)
        if len(lista_tokens) > 1:
            # Encontrar la longitud del prefijo común
            min_len = min(len(t) for t in lista_tokens)
            prefijo = []
            
            for i in range(min_len):
                token_actual = lista_tokens[0][i]
                if all(t[i] == token_actual for t in lista_tokens):
                    prefijo.append(token_actual)
                else:
                    break
            
            # Guardar la nueva regla factorizada (Prefijo + Nuevo_NT)
            str_prefijo = " ".join(prefijo)
            nuevas_reglas_base.append(f"{str_prefijo} {nuevo_nt}")
            
            # Generar los remanentes para el Nuevo No-Terminal
            len_pref = len(prefijo)
            for t in lista_tokens:
                resto = t[len_pref:]
                if not resto:
                    nuevas_reglas_prima.append("ε") # Epsilon (cadena vacía)
                else:
                    nuevas_reglas_prima.append(" ".join(resto))
        else:
            # Si no hay conflicto en este grupo, la regla pasa intacta
            nuevas_reglas_base.append(" ".join(lista_tokens[0]))
            
    # 3. Ensamblar el diccionario final
    resultado = {no_terminal: nuevas_reglas_base}
    if nuevas_reglas_prima:
        resultado[nuevo_nt] = nuevas_reglas_prima
        
    return resultado

# ==========================================
# EJECUCIÓN DEL CASO PRÁCTICO PARA EL INFORME
# ==========================================
if __name__ == "__main__":
    # Caso 2.3.1 c) Patologías de las gramáticas
    estado_inicial = "S"
    
    # Lista de producciones (puedes cambiar el orden y funcionará perfecto)
    reglas = [
        "if E then S",
        "if E then S else S",
        "a",
        "b"
    ]
    
    print("=== GRAMÁTICA ORIGINAL (CON AMBIGÜEDAD DE PREFIJO) ===")
    for r in reglas:
        print(f"{estado_inicial} -> {r}")
        
    # Ejecutamos la función
    gramatica_optimizada = factorizar_izquierda(estado_inicial, reglas)
    
    print("\n=== GRAMÁTICA RESULTANTE OPTIMIZADA ===")
    for nt, prods in gramatica_optimizada.items():
        # Unimos las reglas con el símbolo '|'
        reglas_str = " | ".join(prods)
        print(f"{nt} -> {reglas_str}")