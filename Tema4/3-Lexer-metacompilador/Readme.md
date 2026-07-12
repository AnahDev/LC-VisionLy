# 🦀 Lexer para MiniRust (Actividad 4.3 - Metacompilador Logos)

## 📝 Descripción

Esta actuvidad (3) implementa un **analizador léxico (lexer)** para un subconjunto del lenguaje de programación **Rust**, denominado **MiniRust**.

El lexer está construido utilizando el metacompilador **Logos**, una librería de Rust que genera autómatas finitos deterministas (AFD) a partir de expresiones regulares y literales definidos en un `enum`.

**¿Qué hace?**

- Lee un archivo fuente escrito en MiniRust.
- Identifica y clasifica los componentes léxicos (tokens) como palabras clave (`fn`, `let`, `if`), identificadores, números, operadores y símbolos.
- Reporta errores léxicos cuando encuentra caracteres o patrones no definidos en el lenguaje (por ejemplo, el uso de `:` en los tipos de datos, que aún no está soportado en esta versión del lexer).

---

### 📌 Tokens Soportados (Actuales)

| Token              | Descripción                            |
| :----------------- | :------------------------------------- |
| Fn                 | Palabra clave fn                       |
| Let                | Palabra clave let                      |
| If / Else          | Palabras clave condicionales           |
| While              | Palabra clave de bucle                 |
| Return             | Palabra clave return                   |
| True / False       | Literales booleanos                    |
| Identifier(String) | Identificadores (ej. variable)         |
| Integer(i64)       | Números enteros                        |
| Float(f64)         | Números flotantes                      |
| String(String)     | Cadenas de texto entre comillas        |
| Plus, Minus, etc   | Operadores aritméticos                 |
| Assign, Eq         | Operadores de asignación y comparación |
| LParen, RParen     | Paréntesis                             |
| LBrace, RBrace     | Llaves                                 |
| Semicolon          | Punto y coma ;                         |
| Comma              | Coma ,                                 |
| Arrow              | Flecha                                 |

## 📋 Requisitos del Sistema

Para compilar y ejecutar este proyecto, necesitas tener instalado:

- **Rust** (compilador `rustc`) y **Cargo** (gestor de paquetes y construcción).
  - Puedes instalarlos desde: [https://rustup.rs/](https://rustup.rs/)
- **(Opcional)** Visual Studio Code con la extensión **rust-analyzer** para una mejor experiencia de desarrollo.

---

## ⚙️ Instalación y Compilación

Sigue estos pasos para obtener el lexer en tu máquina local:

1. **Clonar el repositorio** (o ubicarte dentro de la carpeta del proyecto):

   ```bash
   git clone <url_de_tu_repositorio>
   cd LC-VisionLy/Tema4/3-Lexer-metacompilador
   ```

2. **Compilar el proyecto** (esto descargará las dependencias y generará el binario):

```
cargo build --release
```

También puedes usar `cargo build` para una compilación en modo depuración (más rápida para pruebas).

### 🚀 Uso del Lexer

Una vez compilado, ejecuta el lexer pasando como argumento la ruta del archivo fuente que deseas analizar.

Sintaxis:

```
bash
cargo run -- <ruta_del_archivo>
```

Ejemplo básico:

bash
cargo run -- examples/factorial.minirust

Si prefieres usar el binario compilado directamente (ubicado en target/release/):

./target/release/minirust_lexer.exe examples/factorial.minirust # Windows
./target/release/minirust_lexer examples/factorial.minirust # Linux/Mac

### 🔍 Ejemplos de Ejecución

### Ejemplo 1: Impresion de HOLA MUNDO ( Archivo hello.minirust )

Contenido del archivo (examples/hello.minirust):

```
fn main() {
    let message = "Hola, mundo!";
}
```

### Comando para ejecutarlo:

bash

```
cargo run -- examples/hello.minirust
```

### Salida esperada (simulada):

```
text

Fn, Identifier("main"), LParen, RParen, LBrace,
Let, Identifier("message"), Assign, String("Hola, mundo!"), Semicolon,
RBrace
```
