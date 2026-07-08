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
current_function_type = None
loop_and_switch_depth = 0

# ==========================================
# --- INICIO APORTE DANIEL CORTEZ ---
# ==========================================

# REGLA 1: Alcance de variables (Scope)
def enter_scope():
    global symbol_table
    symbol_table.append({})

def exit_scope():
    global symbol_table
    if len(symbol_table) > 1:
        symbol_table.pop()

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
def check_variable_declared(name):
    pass

def check_reassignment(name):
    pass
# --- FIN APORTE SOFIA IZAGUIRRE ---


# ==========================================
# --- INICIO APORTE ALEXANDER NIEVES ---
# ==========================================
def validate_return_type(return_type):
    pass

def validate_break_continue():
    pass
# --- FIN APORTE ALEXANDER NIEVES ---


# ==========================================
# --- MOTOR DEL ANALIZADOR SEMÁNTICO ---
# ==========================================
def semantic_analysis(lexer) -> str:
    global log, symbol_table
    
    log = ''
    symbol_table = [{}]
    
    from .syntactic import parser
    parser.parse(lexer=lexer)
    
    response = log
    if not response.strip():
        response = "Analisis Semantico Exitoso: No se encontraron errores de Scope o Tipos.\n"
        
    log = ''
    return response