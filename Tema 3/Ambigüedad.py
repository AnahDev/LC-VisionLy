class ParserDescendenteRecursivo:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def obtener_token_actual(self):
        """Devuelve el token en la posición actual de lectura."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def match(self, token_esperado):
        """Avanza si el token actual coincide con el esperado."""
        if self.obtener_token_actual() == token_esperado:
            self.pos += 1
            return True
        return False

    def parse_E(self):
        """
        Regla Expresión (E -> T + E | T)
        Maneja la suma (Menor precedencia).
        """
        nodo_izq = self.parse_T()
        
        # Si encontramos un signo '+', resolvemos la estructura jerárquica
        if self.obtener_token_actual() == '+':
            op = self.obtener_token_actual()
            self.pos += 1 # Consumir el '+'
            nodo_der = self.parse_E()
            return f"[{nodo_izq} {op} {nodo_der}]"
            
        return nodo_izq

    def parse_T(self):
        """
        Regla Término (T -> F * T | F)
        Maneja la multiplicación (Mayor precedencia).
        """
        nodo_izq = self.parse_F()
        
        # Si encontramos un signo '*', se agrupa primero aquí
        if self.obtener_token_actual() == '*':
            op = self.obtener_token_actual()
            self.pos += 1 # Consumir el '*'
            nodo_der = self.parse_T()
            return f"[{nodo_izq} {op} {nodo_der}]"
            
        return nodo_izq

    def parse_F(self):
        """
        Regla Factor (F -> id)
        Maneja los elementos terminales (identificadores o variables).
        """
        token = self.obtener_token_actual()
        if token == 'id':
            self.pos += 1 # Consumir el 'id'
            return "id"
        
        raise SyntaxError(f"Error Sintáctico: Se esperaba 'id', se obtuvo '{token}'")

# ===================================================
# PRUEBA DE RESOLUCIÓN DE AMBIGÜEDAD
# ===================================================
if __name__ == "__main__":
    # Cadena de entrada en forma de tokens: "id + id * id"
    tokens_entrada = ['id', '+', 'id', '*', 'id']
    
    print("Cadena de entrada:", " ".join(tokens_entrada))
    
    # Inicializamos el parser con los tokens
    parser = ParserDescendenteRecursivo(tokens_entrada)
    
    # Comenzamos el análisis desde el axioma inicial (E)
    arbol_sintactico = parser.parse_E()
    
    print("\n--- Árbol Sintáctico Único Generado ---")
    print(arbol_sintactico)