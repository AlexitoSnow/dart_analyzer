import ply.lex as lex

data_types = {
    # --- SOFIA IZAGUIRRE ---
    'int': 'DT_INT',
    'Map': 'DT_MAP',

    # --- DANIEL CORTEZ ---
    'double': 'DT_DOUBLE',
    'bool': 'DT_BOOL',
    'Set': 'DT_SET',

    # --- ALEXANDER NIEVES ---
    'String': 'DT_STRING',
    'List': 'DT_LIST',
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

    # -- ALEXANDER NIEVES ---
    'case': 'KW_CASE',
    'class': 'KW_CLASS',
    'default': 'KW_DEFAULT',
    'null': 'KW_NULL',
}


tokens = (
    # --- SOFIA IZAGUIRRE ---
    'ID',
    'OP_ASSIGN',
    
    'VAL_INT',
    
    # --- DANIEL CORTEZ ---
    'OP_FLECHA',
    'OP_LOGIC',
    'OP_NULLABLE',
    'OP_RELACIONAL',

    'VAL_DOUBLE',
    'VAL_BOOL',
    
    # --- ALEXANDER NIEVES ---
    'OP_ARITHMETIC',
    'OP_DECREMENT',
    'OP_GREATHER',
    'OP_INCREMENT',
    'OP_LESS',
    'OP_SINGLE_INCREMENT',
    'OP_SINGLE_DECREMENT',
    
    'VAL_STRING',
    
    'DEL_LBRACE',
    'DEL_RBRACE',
    'DEL_LPAREN',
    'DEL_RPAREN',
    'DEL_LBRACKET',
    'DEL_RBRACKET',
    'DEL_COLON',
    'DEL_SEMICOLON',
    'DEL_COMMA',
    'DEL_DOT',
) + tuple(data_types.values()) + tuple(keywords.values())

log = ''

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# --- SOFIA IZAGUIRRE ---
t_OP_ASSIGN = r'='

# --- DANIEL CORTEZ ---
t_OP_FLECHA = r'=>'
t_OP_LOGIC = r'&&|\|\||!'
t_OP_NULLABLE = r'\?'
t_OP_RELACIONAL = r'==|!=|>=|<='

# --- ALEXANDER NIEVES ---
t_DEL_LBRACE   = r'\{'
t_DEL_RBRACE   = r'\}'
t_DEL_LBRACKET = r'\['
t_DEL_RBRACKET = r'\]'
t_DEL_LPAREN   = r'\('
t_DEL_RPAREN   = r'\)'
t_DEL_COMMA    = r','
t_DEL_SEMICOLON= r';'
t_DEL_COLON    = r':'
t_DEL_DOT      = r'\.'

t_OP_ARITHMETIC = r'\+|-|\*|/|%'
t_OP_DECREMENT = r'-='
t_OP_GREATHER = r'>'
t_OP_INCREMENT = r'\+='
t_OP_LESS = r'<'

def t_ignore_comment(t):
    # Reconoce comentarios de una y múltiples líneas
    r'(//.*)|(/\*(.|\n)*?\*/)'
    t.lexer.lineno += t.value.count('\n')
    pass

# Funciones para dar prioridad
def t_OP_SINGLE_INCREMENT(t):
    r'\+\+'
    return t

def t_OP_SINGLE_DECREMENT(t):
    r'--'
    return t

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

# --- ALEXANDER NIEVES ---
def t_VAL_STRING(t):
    # Reconoce cadenas de texto
    r'"([^\\]|\\.)*?"|\'([^\\]|\\.)*?\''
    t.value = t.value[1:-1]
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

def lexical_analysis(lexer_instance) -> str:
    global log

    while True:
        token = lexer_instance.token()
        if not token:
            break
        log += str(token) + '\n'
    
    response = log
    log = ''
    return response