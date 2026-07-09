import ply.yacc as yacc
from .lexical import tokens
from . import semantic 
from .semantic import declare_variable, check_variable_declared, check_reassignment

log = ''

# ==========================================
# --- ESTRUCTURA BASE (COLABORATIVO) ---
# ==========================================
def p_programa(p):
    '''programa : instruction
                | programa instruction'''

def p_instruction(p):
    '''instruction : variable_declaration
                   | expressions
                   | reasignacion
                   | control_structures
                   | data_structures
                   | function_declarations
                   | class_declaration
                   | input_output
                   | KW_BREAK DEL_SEMICOLON
                   | KW_RETURN DEL_SEMICOLON
                   | KW_RETURN arithmetic_expression DEL_SEMICOLON
                   | KW_RETURN boolean_expression DEL_SEMICOLON
                   | KW_RETURN valor DEL_SEMICOLON
                   | ID instruction
                   | error DEL_SEMICOLON
                   | error DEL_RBRACE'''
    p[0] = p[1]
    if isinstance(p[1], str):
        if p[1] == 'break':
            semantic.validate_break_continue('break', line=p.lineno(1))
        elif p[1] == 'return':
            if len(p) == 3:
                semantic.validate_return_type('void', line=p.lineno(1))
            elif len(p) == 4:
                expr_type = 'void'
                symbol_type = p.slice[2].type
                if symbol_type == 'arithmetic_expression':
                    expr_type = semantic.get_type_of_val(p[2])
                    if expr_type not in ['int', 'double']:
                        expr_type = 'int'
                elif symbol_type == 'boolean_expression':
                    expr_type = 'bool'
                elif symbol_type == 'valor':
                    expr_type = semantic.get_type_of_val(p[2])
                semantic.validate_return_type(expr_type, line=p.lineno(1))

# --- REGLAS MARCADORAS DE SCOPE ---
def p_open_scope(p):
    '''open_scope : DEL_LBRACE'''
    semantic.enter_scope() 
    p[0] = p[1]

def p_close_scope(p):
    '''close_scope : DEL_RBRACE'''
    semantic.exit_scope() 
    p[0] = p[1]

# --- REGLAS MARCADORAS DE CONTROL FLOW ---
def p_enter_loop(p):
    '''enter_loop : '''
    semantic.loop_and_switch_depth += 1

def p_exit_loop(p):
    '''exit_loop : '''
    semantic.loop_and_switch_depth -= 1
# -------------------------------------------------------

def p_variable_declaration(p):
    '''variable_declaration : vd_inmutability
                            | vd_nullability
                            | vd_inference
                            | vd_static'''
    p[0] = p[1]

def p_expressions(p):
    '''expressions : arithmetic_expression
                   | boolean_expression
                   | ID OP_SINGLE_INCREMENT DEL_SEMICOLON
                   | ID OP_SINGLE_DECREMENT DEL_SEMICOLON'''
    if len(p) == 4 and p[2] in ['++', '--']:
        semantic.get_variable(p[1], line=p.lineno(1))
    p[0] = p[1]

def p_control_structures(p):
    '''control_structures : ce_if_else
                        | ce_while
                        | ce_for
                        | ce_switch'''
    p[0] = p[1]

def p_data_structures(p):
    '''data_structures : de_list
                        | de_map
                        | de_set'''
    p[0] = p[1]

def p_function_declarations(p):
    '''function_declarations : fd_void
                            | fd_return
                            | fd_lambda'''
    p[0] = p[1]

def p_input_output(p):
    '''input_output : io_print
                    | io_read'''
    p[0] = p[1]

def p_body(p):
    '''body : instructions
            | empty'''
    pass

def p_instructions(p):
    '''instructions : instruction
                    | instructions instruction'''
    pass

def p_empty(p):
    '''empty : '''
    pass

def p_data_type(p):
    '''data_type : DT_INT
                 | DT_DOUBLE
                 | DT_BOOL
                 | DT_STRING
                 | DT_LIST
                 | DT_MAP
                 | DT_SET'''
    p[0] = p[1]

def p_valor(p):
    '''valor : VAL_INT
             | VAL_DOUBLE
             | VAL_BOOL
             | VAL_STRING
             | KW_NULL
             | KW_TRUE
             | KW_FALSE
             | ID'''
    # CORRECCIÓN SEMÁNTICA: Solo busca variables si el token es estrictamente de tipo ID
    if len(p) == 2 and p.slice[1].type == 'ID' and p[1] not in ['true', 'false', 'null']:
        semantic.check_variable_declared(p[1], line=p.lineno(1))
    p[0] = p[1]

def p_error(p):
    global log
    if p:
        message = f"Error Sintactico: Estructura no valida cerca de '{p.value}' en la linea {p.lineno}"
    else:
        message = "Error Sintactico: Fin de archivo inesperado (falta cerrar algo)"
    log += message + '\n'
    semantic.current_function_type = semantic.function_type_stack[-1] if hasattr(semantic, 'function_type_stack') else None


# ==========================================
# --- INICIO APORTE ALEXANDER NIEVES ---
# ==========================================

# Soporte para Clases 
def p_class_declaration(p):
    '''class_declaration : KW_CLASS ID open_scope class_body close_scope
                         | KW_CLASS ID ID ID open_scope class_body close_scope'''
    global log
    log += f"Declaracion de clase: '{p[2]}'\n"

def p_class_body(p):
    '''class_body : class_instructions
                  | empty'''
    pass

def p_class_instructions(p):
    '''class_instructions : class_instruction
                          | class_instructions class_instruction'''
    pass

def p_class_instruction(p):
    '''class_instruction : instruction
                         | ID instruction'''
    pass

# Declaracion de variable Forma 3 (Inmutabilidad)
def p_vd_inmutability(p):
    '''vd_inmutability : KW_FINAL ID OP_ASSIGN valor DEL_SEMICOLON
                       | KW_FINAL data_type ID OP_ASSIGN valor DEL_SEMICOLON
                       | KW_CONST ID OP_ASSIGN valor DEL_SEMICOLON
                       | KW_CONST data_type ID OP_ASSIGN valor DEL_SEMICOLON'''
    global log
    nombre_var = p[2] if len(p) == 6 else p[3]
    tipo_dato = p[1] if len(p) == 6 else p[2]
    linea = p.lineno(2) if len(p) == 6 else p.lineno(3)
    
    semantic.declare_variable(nombre_var, tipo_dato, is_constant=True, line=linea) 
    log += f"Declaracion de variable: Inmutabilidad '{nombre_var}'\n"

# Expresiones Aritméticas
def p_arithmetic_expression(p):
    '''arithmetic_expression : term OP_ARITHMETIC term
                              | DEL_LPAREN arithmetic_expression DEL_RPAREN
                              | arithmetic_expression OP_ARITHMETIC term'''
    p[0] = p[1]

def p_term(p):
    '''term : VAL_INT
            | VAL_DOUBLE
            | ID'''
    p[0] = p[1]

# Bucle For
def p_for_init(p):
    '''for_init : data_type ID OP_ASSIGN valor'''
    semantic.declare_variable(p[2], p[1], line=p.lineno(2)) # Variable 'i' registrada
    p[0] = p[2]

def p_ce_for(p):
    '''ce_for : KW_FOR DEL_LPAREN for_init DEL_SEMICOLON for_condition DEL_SEMICOLON for_step DEL_RPAREN enter_loop open_scope body close_scope exit_loop'''
    global log
    log += f"Estructura de control: For\n"
    p[0] = p[1]

def p_for_condition(p):
    '''for_condition : ID OP_RELACIONAL valor
                    | valor OP_RELACIONAL ID
                    | ID OP_LESS valor
                    | valor OP_LESS ID
                    | ID OP_GREATHER valor
                    | valor OP_GREATHER ID'''
    p[0] = p[1]

def p_for_step(p):
    '''for_step : ID OP_SINGLE_DECREMENT
                | ID OP_SINGLE_INCREMENT
                | ID OP_DECREMENT valor
                | ID OP_INCREMENT valor'''

# Estructura Switch
def p_ce_switch(p):
    '''ce_switch : KW_SWITCH DEL_LPAREN ID DEL_RPAREN enter_loop open_scope switch_cases close_scope exit_loop'''
    global log
    log += "Estructura de control: Switch\n"

def p_switch_cases(p):
    '''switch_cases : switch_case
                    | switch_cases switch_case
                    | empty'''
    pass

def p_switch_case(p):
    '''switch_case : KW_CASE valor DEL_COLON body
                   | KW_DEFAULT DEL_COLON body'''
    pass

# Colecciones: List
def p_de_list(p):
    '''de_list : DT_LIST ID OP_ASSIGN DEL_LBRACKET list_content DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST ID OP_ASSIGN DEL_LBRACKET DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACKET list_content DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACKET DEL_RBRACKET DEL_SEMICOLON'''
    global log
    if p[2] == '<':
        nombre_var, linea = p[5], p.lineno(5)
    else:
        nombre_var, linea = p[2], p.lineno(2)
        
    semantic.declare_variable(nombre_var, 'DT_LIST', line=linea)
    log += f"Declaracion de estructura: List '{nombre_var}'\n"
    p[0] = p[1]

def p_list_content(p):
    '''list_content : valor
                    | list_content DEL_COMMA valor'''
    p[0] = p[1]

# Funciones Void
def p_fd_void_header(p):
    '''fd_void_header : KW_VOID ID DEL_LPAREN parameters DEL_RPAREN
                      | KW_VOID ID DEL_LPAREN DEL_RPAREN'''
    semantic.current_function_type = 'void'
    p[0] = p[2]

def p_fd_void(p):
    '''fd_void : fd_void_header open_scope body close_scope'''
    global log
    log += f"Declaracion de funcion: Void '{p[1]}'\n"
    semantic.current_function_type = None
    p[0] = 'void'

def p_parameters(p):
    '''parameters : parameter
                  | parameters DEL_COMMA parameter
                  | empty'''
    p[0] = p[1]

def p_parameter(p):
    '''parameter : data_type ID
                 | data_type OP_NULLABLE ID'''
    p[0] = p[1]
# --- FIN APORTE ALEXANDER NIEVES ---


# ==========================================
# --- INICIO APORTE SOFIA IZAGUIRRE ---
# ==========================================

# Declaracion de variable Forma 1 (Inferencia)
def p_vd_inference(p):
    '''vd_inference : KW_VAR ID OP_ASSIGN valor DEL_SEMICOLON
                    | KW_VAR ID OP_ASSIGN arithmetic_expression DEL_SEMICOLON'''
    global log
    semantic.declare_variable(p[2], 'KW_VAR', line=p.lineno(2)) 
    log += f"Declaracion de variable: Inferencia de tipo '{p[2]}'\n"

# Expresiones booleanas
def p_boolean_expression(p):
    '''boolean_expression : valor OP_RELACIONAL valor
                          | valor OP_LESS valor
                          | valor OP_GREATHER valor
                          | DEL_LPAREN boolean_expression DEL_RPAREN
                          | boolean_expression OP_LOGIC boolean_expression
                          | OP_LOGIC boolean_expression
                          | OP_LOGIC valor
                          | KW_TRUE
                          | KW_FALSE'''
    p[0] = p[1]

# Condicional If/Else
def p_ce_if_else(p):
    '''ce_if_else : KW_IF DEL_LPAREN boolean_expression DEL_RPAREN open_scope body close_scope
                  | KW_IF DEL_LPAREN boolean_expression DEL_RPAREN open_scope body close_scope KW_ELSE open_scope body close_scope'''
    global log
    if len(p) == 8:
        log += "Estructura de control: IF\n"
    else:
        log += "Estructura de control: IF-ELSE\n"

# Colecciones: Map
def p_de_map(p):
    '''de_map : DT_MAP OP_LESS data_type DEL_COMMA data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACE map_elements DEL_RBRACE DEL_SEMICOLON
              | DT_MAP ID OP_ASSIGN DEL_LBRACE map_elements DEL_RBRACE DEL_SEMICOLON
              | DT_MAP OP_LESS data_type DEL_COMMA data_type OP_GREATHER OP_NULLABLE ID DEL_SEMICOLON
              | DT_MAP OP_NULLABLE ID DEL_SEMICOLON'''
    global log
    nombre_var = p[7] if len(p) == 13 else (p[2] if len(p) == 8 else (p[8] if len(p) == 10 else p[3]))
    linea = p.lineno(7) if len(p) == 13 else (p.lineno(2) if len(p) == 8 else (p.lineno(8) if len(p) == 10 else p.lineno(3)))
    
    semantic.declare_variable(nombre_var, 'DT_MAP', line=linea)
    log += f"Declaracion de estructura: Map\n"

def p_map_elements(p):
    '''map_elements : valor DEL_COLON valor
                    | valor DEL_COLON valor DEL_COMMA map_elements
                    | empty'''
    pass

def p_fd_return_header(p):
    '''fd_return_header : data_type ID DEL_LPAREN parameters DEL_RPAREN
                        | data_type ID DEL_LPAREN DEL_RPAREN'''
    semantic.current_function_type = p[1]
    p[0] = (p[1], p[2])

# Declaracion de funcion estandar con retorno
def p_fd_return(p):
    '''fd_return : fd_return_header open_scope body close_scope'''
    global log
    log += f"Declaracion de funcion: Retorno '{p[1][1]}'\n"
    semantic.current_function_type = None

# Validacion de reasignacion para constantes (Regla Semántica 2)
def p_reasignacion(p):
    '''reasignacion : ID OP_ASSIGN valor DEL_SEMICOLON
                    | ID OP_ASSIGN arithmetic_expression DEL_SEMICOLON
                    | ID OP_ASSIGN boolean_expression DEL_SEMICOLON'''
    global log
    # VALIDACIÓN SEMÁNTICA: Verifica que no sea constante
    semantic.check_reassignment(p[1], line=p.lineno(1))
    log += f"Reasignacion de variable: '{p[1]}'\n"

# --- FIN APORTE SOFIA IZAGUIRRE ---


# ==========================================
# --- INICIO APORTE DANIEL CORTEZ ---
# ==========================================

# Declaracion de variable Forma 4 (Nulabilidad)
def p_vd_nullability(p):
    '''vd_nullability : data_type OP_NULLABLE ID DEL_SEMICOLON
                      | data_type OP_NULLABLE ID OP_ASSIGN valor DEL_SEMICOLON'''
    global log
    semantic.declare_variable(p[3], p[1], line=p.lineno(3))
    if len(p) == 5:
        message = f"Declaracion de variable nulable: '{p[3]}'"
    else:
        message = f"Declaracion de variable nulable con valor: '{p[3]}' = {p[5]}"
    log += message + '\n'

# Declaracion de variable Forma 2 (Tipado Estático)
def p_vd_static(p):
    '''vd_static : data_type ID OP_ASSIGN valor DEL_SEMICOLON
                 | data_type ID DEL_SEMICOLON
                 | data_type ID OP_ASSIGN arithmetic_expression DEL_SEMICOLON
                 | data_type ID OP_ASSIGN boolean_expression DEL_SEMICOLON'''
    global log
    semantic.declare_variable(p[2], p[1], line=p.lineno(2)) 
    log += f"Declaracion de variable: Tipado estatico '{p[2]}'\n"

# Bucle While
def p_ce_while(p):
    '''ce_while : KW_WHILE DEL_LPAREN boolean_expression DEL_RPAREN enter_loop open_scope body close_scope exit_loop'''
    global log
    log += "Estructura de control: While\n"

# Colecciones: Set
def p_de_set(p):
    '''de_set : DT_SET OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACE set_elements DEL_RBRACE DEL_SEMICOLON
              | DT_SET ID OP_ASSIGN DEL_LBRACE set_elements DEL_RBRACE DEL_SEMICOLON
              | DT_SET OP_LESS data_type OP_GREATHER OP_NULLABLE ID DEL_SEMICOLON
              | DT_SET OP_NULLABLE ID DEL_SEMICOLON'''
    global log
    if len(p) == 11:
        nombre_var, linea = p[5], p.lineno(5)
    elif len(p) == 8 and p[2] == '<':
        nombre_var, linea = p[6], p.lineno(6)
    elif len(p) == 8:
        nombre_var, linea = p[2], p.lineno(2)
    else:
        nombre_var, linea = p[3], p.lineno(3)
        
    semantic.declare_variable(nombre_var, 'DT_SET', line=linea)
    log += f"Declaracion de estructura: Set\n"

def p_set_elements(p):
    '''set_elements : valor
                    | valor DEL_COMMA set_elements
                    | empty'''
    pass

# Funcion lambda/flecha
def p_fd_lambda(p):
    '''fd_lambda : fd_return_header OP_FLECHA arithmetic_expression DEL_SEMICOLON
                 | fd_return_header OP_FLECHA boolean_expression DEL_SEMICOLON
                 | fd_return_header OP_FLECHA valor DEL_SEMICOLON'''
    global log
    log += f"Declaracion de funcion: Lambda '{p[1][1]}'\n"
    semantic.current_function_type = None

# Impresión y Solicitud de datos
def p_io_print(p):
    '''io_print : KW_PRINT DEL_LPAREN print_content DEL_RPAREN DEL_SEMICOLON'''
    global log
    log += "Impresion de datos: print\n"

def p_print_content(p):
    '''print_content : arithmetic_expression
                     | boolean_expression
                     | valor'''
    pass

def p_io_read(p):
    '''io_read : data_type OP_NULLABLE ID OP_ASSIGN ID DEL_DOT ID DEL_LPAREN DEL_RPAREN DEL_SEMICOLON'''
    global log
    log += f"Solicitud de datos: readLineSync a la variable '{p[3]}'\n"
# --- FIN APORTE DANIEL CORTEZ ---

parser = yacc.yacc()

def syntactic_analysis(lexer) -> str:
    global log

    log = ''
    parser.parse(lexer=lexer)
    response = log
    log = ''

    return response