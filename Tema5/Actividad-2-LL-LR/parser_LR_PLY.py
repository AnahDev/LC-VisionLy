
import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = ('NUM', 'VAR', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Lex error: illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Definición de la gramática (recursión izquierda)
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = BinOp(p[1], '+', p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = BinOp(p[1], '-', p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = BinOp(p[1], '*', p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = BinOp(p[1], '/', p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUM'
    p[0] = Num(p[1])

def p_factor_var(p):
    'factor : VAR'
    p[0] = Var(p[1])

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# Función para evaluar el AST (opcional)
def evaluate_ast(node, env={}):
    if isinstance(node, Num):
        return node.value
    elif isinstance(node, Var):
        return env.get(node.name, 0)
    elif isinstance(node, BinOp):
        left_val = evaluate_ast(node.left, env)
        right_val = evaluate_ast(node.right, env)
        if node.op == '+':
            return left_val + right_val
        elif node.op == '-':
            return left_val - right_val
        elif node.op == '*':
            return left_val * right_val
        elif node.op == '/':
            return left_val / right_val
        else:
            raise ValueError(f"Unknown operator {node.op}")
    else:
        raise TypeError(f"Unknown node type {type(node)}")

# Ejemplo de uso
if __name__ == '__main__':
    expr = "3 + 5 * 2"
    ast_lr = parser.parse(expr, lexer=lexer)
    print("AST (LR) para '3 + 5 * 2':")
    print_ast(ast_lr)
    print("Evaluación:", evaluate_ast(ast_lr))

    expr2 = "x + 2 * y"
    ast_lr2 = parser.parse(expr2, lexer=lexer)
    print("\nAST (LR) para 'x + 2 * y':")
    print_ast(ast_lr2)
    # Evaluar con entorno
    env = {'x': 10, 'y': 3}
    print(f"Evaluación con x=10, y=3: {evaluate_ast(ast_lr2, env)}")