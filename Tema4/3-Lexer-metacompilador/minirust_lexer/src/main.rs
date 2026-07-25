mod tokens;

use logos::Logos;
use std::env;
use std::fs;
use tokens::Token;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Uso: {} <archivo_minirust>", args[0]);
        std::process::exit(1);
    }

    let filename = &args[1];
    let content = fs::read_to_string(filename).expect("Error al leer el archivo");

    println!("===== TOKENS ENCONTRADOS =====");
    let mut lex = Token::lexer(&content);
    while let Some(token) = lex.next() {
        match token {
            Ok(t) => {
                let span = lex.span();
                let line = content[..span.start].matches('\n').count() + 1;
                println!("{:?} en línea {}: '{}'", t, line, &content[span]);
            }
            Err(_e) => {
                let span = lex.span();
                let line = content[..span.start].matches('\n').count() + 1;
                eprintln!("Error léxico en línea {}: '{}'", line, &content[span]);
            }
        }
    }
}
