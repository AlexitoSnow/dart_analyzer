import ply.lex as lex

tokens = (
    # Identificadores
    'ID', 'DELIMITER',
    
    # Palabras Reservadas
    'VAR', 'FINAL', 'CONST',
    'TRUE', 'FALSE',
    'IF', 'ELSE', 'FOR', 'WHILE',
    'RETURN', 'PRINT', 'SWITCH', 'BREAK', 'VOID',
    
    # Tipos de datos 
    'INT', 'DOUBLE', 'STRING', 'BOOL',
    'MAP', 'SET', 'LIST',
    
    # Operador de asignación
    'ASSIGN',
)

# PALABRAS RESERVADAS - DESARROLLADOR 1
reserved = {
    'var': 'VAR',
    'final': 'FINAL',
    'const': 'CONST',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'for': 'FOR',
    'while': 'WHILE',
    'print': 'PRINT',
    'switch': 'SWITCH',
    'break': 'BREAK',
    'void': 'VOID',
    'int': 'INT',
    'Map': 'MAP',
    'double': 'DOUBLE',
    'String': 'STRING',
    'bool': 'BOOL',
    'Set': 'SET',
    'List': 'LIST',
}
# FIN PALABRAS RESERVADAS - DESARROLLADOR 1

log = ''

t_DELIMITER = r'[\(\);]\w*'

# OPERADOR DE ASIGNACIÓN - DESARROLLADOR 1
t_ASSIGN = r'='

# REGLAS PARA IDENTIFICADORES - DESARROLLADOR 1 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t
# FIN DESARROLLADOR 1

def t_COMMENT(t):
    r'//.*'
    t.lexer.skip(len(t.value))

def t_error(t):
    global log

    print(f"Caracter ilegal: '{t.value[0]}'")

    log += f'Caracter ilegal: {t.value[0]}\n'
    t.lexer.skip(1)

lexer = lex.lex()

def lexical_analysis(data: str) -> str:
    global log
    
    lexer.input(data)

    while True:
        token = lexer.token()
        if not token:
            break
        log += str(token) + '\n'
    
    response = log
    log = ''
    return response
