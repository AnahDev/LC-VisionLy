import re

# Clases para los nodos del AST
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Var:
    def __init__(self, name):
        self.name = name

# Parser recursivo descendente para gramática:
# E -> T (('+'|'-') T)*
# T -> F (('*'|'/') F)*
# F -> NUM | VAR | '(' E ')'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse_E(self):
        # E -> T (('+'|'-') T)*
        node = self.parse_T()
        while self.peek() and self.peek()[0] in ('+', '-'):
            op = self.consume()[0]
            right = self.parse_T()
            node = BinOp(node, op, right)
        return node

    def parse_T(self):
        # T -> F (('*'|'/') F)*
        node = self.parse_F()
        while self.peek() and self.peek()[0] in ('*', '/'):
            op = self.consume()[0]
            right = self.parse_F()
            node = BinOp(node, op, right)
        return node

    def parse_F(self):
        tok = self.consume()
        if tok[0] == 'NUM':
            return Num(int(tok[1]))
        elif tok[0] == 'VAR':
            return Var(tok[1])
        elif tok[0] == '(':
            node = self.parse_E()
            if self.peek() and self.peek()[0] == ')':
                self.consume()
                return node
            else:
                raise SyntaxError("Missing closing parenthesis")
        else:
            raise SyntaxError(f"Unexpected token {tok}")

# Función para tokenizar una expresión
def tokenize(expr):
    token_spec = [
        ('NUM', r'\d+'),
        ('VAR', r'[a-zA-Z_]\w*'),
        ('OP', r'[+\-*/]'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SKIP', r'\s+'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
    tokens = []
    for mo in re.finditer(tok_regex, expr):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        tokens.append((kind, value))
    return tokens

# Función para imprimir el AST en formato texto (preorden)
def print_ast(node, indent=0):
    if isinstance(node, Num):
        print('  ' * indent + f'Num({node.value})')
    elif isinstance(node, Var):
        print('  ' * indent + f'Var({node.name})')
    elif isinstance(node, BinOp):
        print('  ' * indent + f'BinOp({node.op})')
        print_ast(node.left, indent+1)
        print_ast(node.right, indent+1)

# Ejemplo de uso
if __name__ == '__main__':
    expr = "3 + 5 * 2"
    tokens = tokenize(expr)
    parser = Parser(tokens)
    ast = parser.parse_E()
    print("AST para '3 + 5 * 2':")
    print_ast(ast)

    expr2 = "x = (10 + y) * 2"  # Nota: no incluimos '=' en la gramática, solo para ilustrar
    # Para este ejemplo, la gramática no soporta asignación, pero podemos extenderla.
    # Mostramos un AST similar:
    print("\nAST conceptual para 'x = (10 + y) * 2':")
    # Simulamos el AST:
    #   '=' nodo con hijo izquierdo Var('x') y derecho un BinOp('*') con izquierda BinOp('+')...
    ast2 = BinOp(Var('x'), '=', BinOp(BinOp(Num(10), '+', Var('y')), '*', Num(2)))
    print_ast(ast2)