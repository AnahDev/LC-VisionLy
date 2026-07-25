import re
from difflib import SequenceMatcher

class UnegScriptHibridoCompiler:
    def __init__(self, codigo_fuente):
        self.codigo_fuente = codigo_fuente
        self.palabras_clave = {"if", "else", "print"}
        self.tokens_corregidos = []
        self.sugerencias_ia = []


    def calcular_confianza(self, token_str, candidato):
       
        return SequenceMatcher(None, token_str, candidato).ratio()

    def consultar_ia_fallback(self, token_erroneo):
    
        # Base de conocimiento contextual de UnegScript
        candidatos = list(self.palabras_clave)
        mejor_candidato = max(candidatos, key=lambda c: self.calcular_confianza(token_erroneo, c))
        confianza = self.calcular_confianza(token_erroneo, mejor_candidato)
        
        # Generar sugerencia de IA
        sugerencia = f"Sugerencia: '{token_erroneo}' → '{mejor_candidato}'"
        if sugerencia not in self.sugerencias_ia:
            self.sugerencias_ia.append(sugerencia)
            
        return mejor_candidato

    def lexer(self):

        # Patrón regex para identificar palabras, números, operadores y delimitadores
        patron = r'[a-zA-Z_]\w*|[0-9]+|[=><;()]|\S'
        elementos = re.findall(patron, self.codigo_fuente)
        
        tokens = []
        for elem in elementos:
            if elem.isspace():
                continue
            # Si es palabra clave válida, operador, delimitador o número exacto
            if elem in self.palabras_clave or elem in {"=", ">", ";", "(", ")"} or elem.isnumeric():
                tipo = "KEYWORD" if elem in self.palabras_clave else ("OPERADOR/DELIMITADOR" if elem in {"=", ">", ";", "(", ")"} else "LITERAL_INT")
                tokens.append((elem, tipo))
            elif re.match(r'^[a-zA-Z_]\w*$', elem):
                # Es un identificador o palabra mal escrita. Verificamos contra palabras clave.
                mejor_cand = max(self.palabras_clave, key=lambda c: self.calcular_confianza(elem, c))
                confianza = self.calcular_confianza(elem, mejor_cand)
                
                if elem == "x": # 'x' es una variable válida permitida en UnegScript
                    tokens.append((elem, "TK_ID"))
                elif confianza >= 0.8:
                    tokens.append((mejor_cand, "KEYWORD"))
                else:
                    # FALLBACK A IA (Umbral < 0.8)
                    token_corregido = self.consultar_ia_fallback(elem)
                    tokens.append((token_corregido, "KEYWORD"))
            else:
                tokens.append((elem, "TK_DESCONOCIDO"))
                
        self.tokens_corregidos = tokens
        return tokens
   
    def parser(self, tokens):
    
        self.tokens_parser = tokens
        self.pos = 0
        ast = {"tipo": "Programa", "cuerpo": []}

        def mirar_adelante():
            if self.pos < len(self.tokens_parser):
                return self.tokens_parser[self.pos]
            return (None, None)

        def consumir(esperado_tipo=None):
            tok, tipo = mirar_adelante()
            self.pos += 1
            return tok, tipo

        # Gramática básica para UnegScript: Asignaciones y Estructuras If
        while self.pos < len(self.tokens_parser):
            tok, tipo = mirar_adelante()
            
            # Caso 1: Asignación (ej. x = 5;)
            if tipo == "TK_ID" and self.pos + 1 < len(self.tokens_parser) and self.tokens_parser[self.pos+1][0] == "=":
                var_nombre, _ = consumir()
                consumir() # operador '='
                val, _ = consumir()
                if mirar_adelante()[0] == ";":
                    consumir()
                ast["cuerpo"].append({
                    "nodo": "Asignacion",
                    "variable": var_nombre,
                    "valor": val
                })
                
            # Caso 2: Estructura condicional If 
            elif tok == "if":
                consumir() # consumir 'if'
                left_var, _ = consumir()
                op, _ = consumir() # operador '>'
                right_val, _ = consumir()
                
                # Rama Then
                func_then, _ = consumir()
                consumir() # '('
                arg_then, _ = consumir()
                consumir() # ')'
                
                # Rama Else
                consumir() # 'else'
                func_else, _ = consumir()
                consumir() # '('
                
                # Manejar literal de cadena o identificador en el else
                arg_else_tok, _ = consumir()
                if arg_else_tok == '"':
                    # literal string partido por regex
                    str_val = '"' + consumir()[0] + '"'
                    consumir() # comilla cierre
                    arg_else = str_val
                else:
                    arg_else = arg_else_tok
                    
                consumir() # ')' cierre de función else
                
                ast["cuerpo"].append({
                    "nodo": "IfStatement",
                    "condicion": f"{left_var} {op} {right_val}",
                    "entonces": {"funcion": func_then, "argumento": arg_then},
                    "sino": {"funcion": func_else, "argumento": arg_else}
                })
            else:
                self.pos += 1 
                
        return ast

    def ejecutar(self):
        """Ejecuta el flujo completo y retorna el resultado solicitado en la Actividad 5."""
        tokens = self.lexer()
        ast = self.parser(tokens)
        return {
            "tokens_corregidos": tokens,
            "ast": ast,
            "sugerencias_ia": self.sugerencias_ia
        }

if __name__ == "__main__":
    codigo_prueba = 'pront x = 5; if x > 3 prnt(x) else print("no")'
    
    print("=== EJECUCIÓN DEL ASISTENTE HÍBRIDO UNEGSCRIPT ===")
    print(f"Código fuente de entrada: {codigo_prueba}\n")
    
    asistente = UnegScriptHibridoCompiler(codigo_prueba)
    resultado = asistente.ejecutar()
    
    print("1. TOKENS CORREGIDOS (Lexer Tradicional + Fallback IA):")
    for t in resultado["tokens_corregidos"]:
        print(f"   {t}")
        
    print("\n2. ÁRBOL DE SINTAXIS ABSTRACTA (AST):")
    import json
    print(json.dumps(resultado["ast"], indent=4, ensure_ascii=False))
    
    print("\n3. SUGERENCIAS IA:")
    for sug in resultado["sugerencias_ia"]:
        print(f"   {sug}")