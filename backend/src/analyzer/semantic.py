# semantic.py

log = ''

class Symbol:
    def __init__(self, name, data_type, is_constant=False):
        self.name = name
        self.data_type = data_type
        self.is_constant = is_constant
        self.is_initialized = False

# --- ESTRUCTURA BASE ---
symbol_table = [{}] 
function_type_stack = [None]
current_function_type = None
loop_and_switch_depth = 0

# ==========================================
# --- INICIO APORTE DANIEL CORTEZ ---
# ==========================================

# REGLA 1: Alcance de variables (Scope)
def enter_scope():
    global symbol_table, function_type_stack, current_function_type
    symbol_table.append({})
    if current_function_type != function_type_stack[-1]:
        function_type_stack.append(current_function_type)
    else:
        function_type_stack.append(function_type_stack[-1])

def exit_scope():
    global symbol_table, function_type_stack, current_function_type
    if len(symbol_table) > 1:
        symbol_table.pop()
        function_type_stack.pop()
        current_function_type = function_type_stack[-1]

def declare_variable(name, data_type, is_constant=False, line=0):
    global log, symbol_table
    current_scope = symbol_table[-1]
    
    if name in current_scope:
        message = f"Error Semantico (Linea {line}): La variable '{name}' ya esta declarada en este alcance."
        print(message)
        log += message + '\n'
        return False
        
    current_scope[name] = Symbol(name, data_type, is_constant)
    
    # Mensaje de Éxito (Opcional, útil para sus pruebas)
    success_msg = f"Semantico (Linea {line}): Variable '{name}' declarada correctamente en memoria."
    print(success_msg)
    # log += success_msg + '\n' # (Descomenta esta línea si quieres que los éxitos salgan en el TXT final)
    
    return True

def get_variable(name, line=0):
    global log, symbol_table
    for scope in reversed(symbol_table):
        if name in scope:
            # Mensaje de Éxito al usar la variable
            print(f"Semantico (Linea {line}): Variable '{name}' encontrada en el scope.")
            return scope[name]
            
    message = f"Error Semantico (Linea {line}): La variable '{name}' esta fuera de alcance (scope) o no ha sido declarada."
    print(message)
    log += message + '\n'
    return None

# REGLA 2: Operaciones permitidas (Compatibilidad de tipos)
def validate_operation(left_type, operator, right_type, line=0):
    global log
    if not left_type or not right_type:
        return None

    if operator in ['+', '-', '*', '/']:
        numeric_types = ['DT_INT', 'DT_DOUBLE']
        if left_type in numeric_types and right_type in numeric_types:
            return 'DT_DOUBLE' if 'DT_DOUBLE' in [left_type, right_type] else 'DT_INT'
        
        if operator == '+' and left_type == 'DT_STRING' and right_type == 'DT_STRING':
            return 'DT_STRING'
            
        message = f"Error Semantico (Linea {line}): Operador '{operator}' no definido para los tipos '{left_type.replace('DT_','')}' y '{right_type.replace('DT_','')}'."
        print(message)
        log += message + '\n'
        return None
        
    elif operator in ['&&', '||']:
        if left_type == 'DT_BOOL' and right_type == 'DT_BOOL':
            return 'DT_BOOL'
        message = f"Error Semantico (Linea {line}): Operador '{operator}' no definido para los tipos '{left_type.replace('DT_','')}' y '{right_type.replace('DT_','')}'."
        print(message)
        log += message + '\n'
        return None
        
    elif operator in ['>', '<', '>=', '<=', '==', '!=']:
        if left_type in ['DT_INT', 'DT_DOUBLE'] and right_type in ['DT_INT', 'DT_DOUBLE']:
            return 'DT_BOOL'
        message = f"Error Semantico (Linea {line}): Operador '{operator}' no definido para los tipos '{left_type.replace('DT_','')}' y '{right_type.replace('DT_','')}'."
        print(message)
        log += message + '\n'
        return None

    return None
# --- FIN APORTE DANIEL CORTEZ ---


# ==========================================
# --- INICIO APORTE SOFIA IZAGUIRRE ---
# ==========================================
# REGLA 1: Identificadores (Declaración previa)
def check_variable_declared(name, line=0):
    global log
    # funcion para buscar en la memoria
    symbol = get_variable(name, line)
    
    if symbol is None:
        # Si la variable no existe, generamos mensaje de error 
        message = f"Error Semántico (Línea {line}): La variable '{name}' no ha sido declarada antes de su uso."
        print(message)
        log += message + '\n'
        return False
        
    return True

# REGLA 2: Asignación de tipo (Constantes)
def check_reassignment(name, line=0):
    global log
    # Primero verificamos si existe 
    if not check_variable_declared(name, line):
        return False        
    # La buscamos en la tabla
    symbol = get_variable(name, line)    
    # Verificamos si es una constante
    if symbol and symbol.is_constant:
        message = f"Error Semántico (Línea {line}): No se puede reasignar un valor a la constante '{name}'."
        print(message)
        log += message + '\n'
        return False
        
    return True
# --- FIN APORTE SOFIA IZAGUIRRE ---


# ==========================================
# --- INICIO APORTE ALEXANDER NIEVES ---
# ==========================================
def normalize_type(t):
    if not t:
        return 'void'
    t_map = {
        'DT_INT': 'int',
        'DT_DOUBLE': 'double',
        'DT_BOOL': 'bool',
        'DT_STRING': 'String',
        'DT_LIST': 'List',
        'DT_MAP': 'Map',
        'DT_SET': 'Set',
        'int': 'int',
        'double': 'double',
        'bool': 'bool',
        'String': 'String',
        'List': 'List',
        'Map': 'Map',
        'Set': 'Set',
        'void': 'void',
    }
    return t_map.get(t, t)

def get_type_of_val(val):
    if isinstance(val, bool):
        return 'bool'
    if isinstance(val, int):
        return 'int'
    if isinstance(val, float):
        return 'double'
    if isinstance(val, str):
        if val in ['true', 'false']:
            return 'bool'
        if val == 'null':
            return 'null'
        # Lookup in symbol table
        for scope in reversed(symbol_table):
            if val in scope:
                return normalize_type(scope[val].data_type)
        return 'String'
    return 'void'

def validate_return_type(return_type, line=0):
    global log, current_function_type
    if current_function_type is None:
        return True
    
    declared_type = normalize_type(current_function_type)
    actual_type = normalize_type(return_type)
    
    if actual_type != 'null' and declared_type != actual_type:
        if declared_type not in ['KW_VAR', 'var']:
            message = f"Error Semántico (Línea {line}): El tipo de retorno '{actual_type}' no coincide con el tipo '{declared_type}' declarado en la función."
            print(message)
            log += message + '\n'
            return False
    return True

def validate_break_continue(statement='break', line=0):
    global log, loop_and_switch_depth
    if loop_and_switch_depth <= 0:
        message = f"Error Semántico (Línea {line}): La sentencia '{statement}' solo puede usarse dentro de un bucle o switch."
        print(message)
        log += message + '\n'
        return False
    return True
# --- FIN APORTE ALEXANDER NIEVES ---


# ==========================================
# --- MOTOR DEL ANALIZADOR SEMÁNTICO ---
# ==========================================
def semantic_analysis(lexer) -> str:
    global log, symbol_table, function_type_stack, current_function_type, loop_and_switch_depth
    
    log = ''
    symbol_table = [{}]
    function_type_stack = [None]
    current_function_type = None
    loop_and_switch_depth = 0
    
    from .syntactic import parser
    parser.parse(lexer=lexer)
    
    response = log
    if not response.strip():
        response = "Analisis Semantico Exitoso: No se encontraron errores de Scope o Tipos.\n"
        
    log = ''
    return response