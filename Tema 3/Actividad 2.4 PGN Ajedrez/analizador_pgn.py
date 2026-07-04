import sys

def analizador_lexico_pgn(cadena):
    # Definición de conjuntos de símbolos del alfabeto
    piezas = {'K', 'Q', 'R', 'B', 'N'}
    columnas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    filas = {'1', '2', '3', '4', '5', '6', '7', '8'}
    digitos_no_cero = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    todos_los_digitos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # Estado inicial
    estado = "q0"
    
    print(f"Analizando cadena: '{cadena}'")
    print(f"[{estado}] -> Inicio del analisis")

    for i, caracter in enumerate(cadena):
        estado_anterior = estado
        
        #Transiciones del AFD 
        if estado == "q0":
            if caracter in digitos_no_cero:
                estado = "q1"
            else:
                estado = "qe"

        elif estado == "q1":
            if caracter in todos_los_digitos:
                estado = "q1"
            elif caracter == ".":
                estado = "q2"
            else:
                estado = "qe"

        elif estado == "q2":
            if caracter in piezas:
                estado = "q3"
            elif caracter in columnas:
                estado = "q4"
            else:
                estado = "qe"

        elif estado == "q3":
            if caracter in columnas:
                estado = "q4"
            else:
                estado = "qe"

        elif estado == "q4":
            if caracter in filas:
                estado = "q5"
            else:
                estado = "qe"

        elif estado == "q5":
            if caracter == " ":
                estado = "q6"
            else:
                estado = "qe"

        elif estado == "q6":
            if caracter in piezas:
                estado = "q7"
            elif caracter in columnas:
                estado = "q8"
            else:
                estado = "qe"

        elif estado == "q7":
            if caracter in columnas:
                estado = "q8"
            else:
                estado = "qe"

        elif estado == "q8":
            if caracter in filas:
                estado = "q10"
            else:
                estado = "qe"

        elif estado == "q10":
            # Si ya estamos en el estado de aceptación y vienen más caracteres,
            # la cadena excede el formato de una jugada simple.
            estado = "qe"

        # Si cae en estado de error, rompemos el ciclo (Early exit)
        if estado == "qe":
            print(f"  Error en carácter '{caracter}' (posición {i}): Transición inválida desde {estado_anterior}.")
            return False, f"Rechazada: Error sintáctico en la posición {i} ('{caracter}')"
        
        print(f"  Tránsito: '{caracter}' -> [{estado}]")

    # --- Verificación del Estado Final ---
    if estado == "q10":
        return True, "¡Cadena ACEPTADA! Sintaxis de jugada PGN válida."
    else:
        return False, f"Rechazada: La cadena terminó en el estado incompleto [{estado}]."


# Casos de Prueba para Demostración
if __name__ == "__main__":
    pruebas = [
        "1.e4 e5",       # Válida (Peones)
        "12.Nf3 d6",     # Válida (Pieza blanca, Peon negro, Nro multiple digito)
        "3.Qd1 Qh5",     # Válida (Ambas piezas mayores)
        "1.e9 e5",       # Inválida (Fila 9 no existe)
        "1.x4 e5",       # Inválida (Columna x no existe)
        "1.e4",          # Inválida (Falta el movimiento de las negras)
        "01.e4 e5"       # Inválida (No puede empezar con cero)
    ]

    print("=== EJECUCIÓN DEL COMPILADOR (ANALIZADOR PGN) ===\n")
    for cadena in pruebas:
        es_valida, mensaje = analizador_lexico_pgn(cadena)
        print(f"Resultado final: {mensaje}")
        print("-" * 50)