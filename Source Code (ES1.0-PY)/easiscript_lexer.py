import ply.lex as lex

# List of token names
tokens = [
    'PRINT', 'STRING', 'SEMICOLON', 'LENGTH_OF',
    'TRUE_VALUE', 'FALSE_VALUE', 'NULL', 'IF', 'ELSE',
    'WHILE', 'FOR', 'RETURN', 'AND', 'OR', 'NOT',
    'EQ', 'NEQ', 'GT', 'LT', 'GTE', 'LTE', 'ASSIGN',
    'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'ID', 'NUMBER',
    'LPAREN', 'RPAREN', 'COMMA', 'DOT'
]

# Regular expression rules for simple tokens
t_PRINT = r'print'
t_STRING = r'\"[^"]*\"'
t_SEMICOLON = r';'
t_LENGTH_OF = r'length_of'
t_TRUE_VALUE = r'true'
t_FALSE_VALUE = r'false'
t_NULL = r'null'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_RETURN = r'return'
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_ASSIGN = r'='
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOT = r'\.'

# Ignore whitespace
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
