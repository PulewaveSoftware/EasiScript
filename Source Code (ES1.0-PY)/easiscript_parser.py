import ply.yacc as yacc
from easiscript_lexer import tokens, lexer

# Parsing rules
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMICOLON'
    print(f"PRINT statement: {p[3]}")

def p_statement_length_of(p):
    'statement : LENGTH_OF LPAREN expression RPAREN SEMICOLON'
    print(f"LENGTH_OF statement: {len(p[3])}")

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1][1:-1]  # Remove quotes

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = int(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression MOD expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_statement_error(p):
    'statement : error SEMICOLON'
    print(f"Syntax error at '{p[1]}'")

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

def parse_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return parser.parse(data, lexer=lexer)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python easiscript_parser.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        result = parse_file(filename)
        print("Parsing result:")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
