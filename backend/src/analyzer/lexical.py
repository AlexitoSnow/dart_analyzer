import ply.lex as lex

# 1. DICCIONARIO DE PALABRAS RESERVADAS
data_types = {
    # --- SOFIA IZAGUIRRE ---
    'int': 'DT_INT',
    'Map': 'DT_MAP',

    # --- DANIEL CORTEZ ---
    'double': 'DT_DOUBLE',
    'bool': 'DT_BOOL',
    'Set': 'DT_SET',
}

keywords = {
    # --- SOFIA IZAGUIRRE ---
    'var': 'KW_VAR',
    'final': 'KW_FINAL',
    'const': 'KW_CONST',
    'true': 'KW_TRUE',
    'false': 'KW_FALSE',
    'if': 'KW_IF',
    'else': 'KW_ELSE',
    'for': 'KW_FOR',
    'while': 'KW_WHILE',
    'return': 'KW_RETURN',
    'print': 'KW_PRINT',
    'switch': 'KW_SWITCH',
    'break': 'KW_BREAK',
    'void': 'KW_VOID',
}


# 2. TUPLA DE TOKENS
tokens = (
    'DELIMITER',
    # --- SOFIA IZAGUIRRE ---
    'ID',
    'OP_ASSIGN',
    
    'VAL_INT',
    
    # --- DANIEL CORTEZ ---
    'OP_ARROW',
    'OP_LOGIC',
    'OP_NULLABLE',
    'OP_RELACIONAL',

    'VAL_DOUBLE',
) + tuple(data_types.values()) + tuple(keywords.values())

log = ''

# Ignorar espacios y tabulaciones
t_ignore = ' \t'


# --- SOFIA IZAGUIRRE ---
t_OP_ASSIGN = r'='

# --- DANIEL CORTEZ ---
t_OP_ARROW = r'=>'
t_OP_LOGIC = r'&&|\|\||!'
t_OP_NULLABLE = r'\?'
t_OP_RELACIONAL = r'==|!=|>=|<=|>|<'

t_DELIMITER = r'[\(\);\{\}\[\],:\.]'

def t_ignore_comment(t):
    # Reconoce comentarios de una y múltiples líneas
    r'(//.*)|(/\*(.|\n)*?\*/)'
    t.lexer.lineno += t.value.count('\n')
    pass

# --- DANIEL CORTEZ ---
def t_VAL_DOUBLE(t):
    # Reconoce numeros decimales
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# --- SOFIA IZAGUIRRE ---
def t_VAL_INT(t):
    # Reconoce números enteros
    r'\d+'
    t.value = int(t.value)
    return t

# --- SOFIA IZAGUIRRE ---
def t_ID(t):
    # Reconoce palabras reservadas o identificadores
    r'[a-zA-Z_]\w*'
    
    t.type = data_types.get(t.value, keywords.get(t.value, 'ID'))
    
    return t

def t_newline(t):
    # Reconoce los saltos de línea
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global log
    message = f'Caracter ilegal: \'{t.value[0]}\' en la linea {t.lineno}'
    print(message)
    log += message + '\n'
    t.lexer.skip(1)

# Construcción del lexer
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