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
    'ID', 'ASSIGN', 'ENTERO',
    # --- FIN APORTE SOFIA IZAGUIRRE ---
    
    # --- INICIO APORTE DANIEL CORTEZ ---
    'RELACIONAL', 'LOGICO', 'FLECHA', 'NULO', 'DECIMAL'
    # --- FIN APORTE DANIEL CORTEZ ---
    
    # [AQUÍ ALEX AÑADIRÁ SUS TOKENS COMO 'ARITMETICO']
) + tuple(data_types.values()) + tuple(keywords.values())

log = ''

# Regla OBLIGATORIA para ignorar espacios y tabulaciones
t_ignore = ' \t'


# 3. DECLARACIÓN DE SÍMBOLOS DIRECTOS

# --- INICIO APORTE SOFIA IZAGUIRRE ---
# Operador de asignación
t_ASSIGN = r'='
# --- FIN APORTE SOFIA IZAGUIRRE ---

# --- INICIO APORTE DANIEL CORTEZ ---
# Operador de Funciones (Lambda)
t_FLECHA = r'=>'
# Operadores relacionales (Importante: los dobles ==, >= van primero que los simples >)
t_RELACIONAL = r'==|!=|>=|<=|>|<'
# Operadores Lógicos (Escapamos el pipe \| porque es especial en regex)
t_LOGICO = r'&&|\|\||!'
# Manejo de nulos (Escapamos la interrogación \?)
t_NULO = r'\?'
# --- FIN APORTE DANIEL CORTEZ ---

# [AQUÍ ALEX AÑADIRÁ SUS SÍMBOLOS COMO t_ARITMETICO]


# --- INICIO APORTE ALEX NIEVES ---
# Delimitador base
t_DELIMITER = r'[\(\);\{\}\[\],:\.]'
# --- FIN APORTE ALEX NIEVES ---


# 4. FUNCIONES DE EVALUACIÓN COMPLEJA

# --- INICIO APORTE SOFIA IZAGUIRRE ---
# Función para Identificadores y filtrado de Palabras Reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verifica si el texto ingresado es una palabra reservada o una variable normal
    t.type = data_types.get(t.value, keywords.get(t.value, 'ID')) 
    return t
# --- FIN APORTE SOFIA IZAGUIRRE ---

# --- INICIO APORTE DANIEL CORTEZ ---
# Reconocer números decimales (ej. 12.5)
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
# --- FIN APORTE DANIEL CORTEZ ---

# --- INICIO APORTE DANIEL CORTEZ ---
# Función robusta para Reglas de Comentarios (De una y múltiples líneas)
def t_COMMENT(t):
    r'(//.*)|(/\*(.|\n)*?\*/)'
    # Contamos los saltos de línea dentro del bloque /* */ para no desajustar el contador de errores
    t.lexer.lineno += t.value.count('\n')
    pass # Usamos pass para que el lexer lo ignore completamente y no lo meta en el log (talvez podriamos quitarlo despues)
# --- FIN APORTE DANIEL CORTEZ ---

# --- INICIO APORTE SOFIA IZAGUIRRE ---
# Reconocer números enteros (ej. 5)
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
# --- FIN APORTE SOFIA IZAGUIRRE ---

# Regla OBLIGATORIA para contar los saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar caracteres no reconocidos
def t_error(t):
    global log
    print(f"Caracter ilegal: '{t.value[0]}' en la linea {t.lineno}")
    log += f"Caracter ilegal: '{t.value[0]}' en la linea {t.lineno}\n"
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