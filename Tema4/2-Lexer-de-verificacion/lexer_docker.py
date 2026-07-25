import re

# 1. Definición de los tokens basados en la sintaxis de Dockerfile
tokens = [
    ('INSTRUCTION', r'^(FROM|RUN|CMD|LABEL|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ARG)\b'),
    ('COMMENT', r'#.*'),
    ('STRING', r'"[^"]*"|\'[^\']*\''),
    ('ARGUMENT', r'[a-zA-Z0-9_./\-:=]+'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.')
]

# 2. Función del Lexer
def lexer(input_text):
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    line_num = 1
    line_start = 0
    
    # Agregamos re.MULTILINE como parámetro, tal como en el código base del profesor
    for mo in re.finditer(token_regex, input_text, re.MULTILINE):
        kind = mo.lastgroup
        value = mo.group(kind)
        
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue 
        elif kind == 'MISMATCH':
            raise RuntimeError(f"ERROR LÉXICO: '{value}' inesperado en la linea {line_num}")
        else:
            column = mo.start() - line_start
            yield kind, value, line_num, column

# 3. Función para cargar el archivo
def cargar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado en Pydroid.")
        return None

# 4.  Crear los archivos automáticamente
def crear_archivos_automaticos():
    f1 = "# Archivo Docker basico\nFROM ubuntu:20.04\nWORKDIR /app\nCOPY . /app\nRUN make /app\nCMD \"python\"\n"
    f2 = "FROM python:3.9-slim\nENV PORT=8080\nEXPOSE 8080\n"
    f3 = "FROM node:14\n?RUN npm install\n"
    
    with open("Docker_ejemplo1.txt", "w") as f: f.write(f1)
    with open("Docker_ejemplo2.txt", "w") as f: f.write(f2)
    with open("Docker_ejemplo3.txt", "w") as f: f.write(f3)

# 5. Bloque principal de ejecución
if __name__ == '__main__':
    crear_archivos_automaticos()
    
    print("=== Analizador Lexico para Docker ===")
    print("(Archivos de prueba generados exitosamente en la memoria)")
    
    nombre_archivo = input("\nEscribe el nombre del archivo (ej. Docker_ejemplo1.txt) y presiona Enter: ")
    nombre_archivo = nombre_archivo.strip() 
    
    input_text = cargar_archivo(nombre_archivo)
    
    if input_text is not None:
        print(f"\n--- Analizando {nombre_archivo} ---")
        try:
            for token in lexer(input_text):
                print(token)
        except RuntimeError as e:
            print(e)
        print("-----------------------------------\n")