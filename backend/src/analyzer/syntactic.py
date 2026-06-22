import ply.yacc as yacc
from .lexical import tokens

log = ''

# --- Alexander Nieves ---
def p_programa(p):
    '''programa : instruction
                | programa instruction'''

def p_instruction(p):
    '''instruction : variable_declaration
                   | expressions
                   | control_structures
                   | data_structures
                   | function_declarations
                   | input_output
                   | error DEL_SEMICOLON
                   | error DEL_RBRACE'''
    p[0] = p[1]

def p_variable_declaration(p):
    '''variable_declaration : vd_inmutability
                            | vd_nullability'''
    # TODO: todas las funciones de declaracion de variables que agreguen listenlas despues del punto, separadas en multilinea con | al inicio
    p[0] = p[1]

def p_expressions(p):
    '''expressions : arithmetic_expression'''
    # TODO: todas las funciones de expresiones que agreguen listenlas despues del punto, separadas en multilinea con | al inicio
    p[0] = p[1]

def p_control_structures(p):
    '''control_structures : ce_if_else
                        | ce_while
                        | ce_for'''
    p[0] = p[1]

def p_data_structures(p):
    '''data_structures : de_list
                        | de_map
                        | de_set'''
    p[0] = p[1]

def p_function_declarations(p):
    '''function_declarations : fd_void'''
    # TODO: todas las funciones de declaracion de funciones que agreguen listenlas despues del punto, separadas en multilinea con | al inicio
    p[0] = p[1]

# --- Quien le toque esta parte :D ---
def p_input_output(p):
    '''input_output : '''
    # TODO: todas las funciones de entrada y salida que agreguen listenlas despues del punto, separadas en multilinea con | al inicio
    p[0] = p[1]

# --- Alexander Nieves ---
def p_vd_inmutability(p):
    '''vd_inmutability : KW_FINAL ID OP_ASSIGN valor DEL_SEMICOLON'''
    global log
    message = f"Declaracion de variable: Inmutabilidad '{p[2]}'"
    log += message + '\n'

# --- Alexander Nieves ---
def p_vd_nullability(p):
    '''vd_nullability : data_type OP_NULLABLE ID DEL_SEMICOLON
                      | data_type OP_NULLABLE ID OP_ASSIGN valor DEL_SEMICOLON'''
    global log
    if len(p) == 5:
        message = f"Declaracion de variable nulable: '{p[3]}'"
    else:
        message = f"Declaracion de variable nulable con valor: '{p[3]}' = {p[5]}"
    log += message + '\n'

# --- Sofia Izaguirre ---
# Declaracion de variable Forma 1

# --- Daniel Cortez ---
# Declaracion de variable Forma 2

# --- Alexander Nieves ---
def p_arithmetic_expression(p):
    '''arithmetic_expression : term OP_ARITHMETIC term
                              | DEL_LPAREN arithmetic_expression DEL_RPAREN
                              | arithmetic_expression OP_ARITHMETIC term'''
    p[0] = p[1]

def p_term(p):
    '''term : VAL_INT
            | VAL_DOUBLE'''
    p[0] = p[1]

# --- Daniel Cortez ---
# Expresiones booleanas

# --- Sofia Izaguirre ---
def p_ce_if_else(p):
    '''ce_if_else : '''
    p[0] = p[1]

# --- Daniel Cortez ---
def p_ce_while(p):
    '''ce_while : '''
    p[0] = p[1]

# --- Alexander Nieves ---
def p_ce_for(p):
    '''ce_for : KW_FOR DEL_LPAREN data_type ID OP_ASSIGN valor DEL_SEMICOLON for_condition DEL_SEMICOLON for_step DEL_RPAREN DEL_LBRACE body DEL_RBRACE'''
    global log
    message = f"Estructura de control: For"
    log += message + '\n'
    p[0] = p[1]

def p_for_condition(p):
    '''for_condition : ID OP_RELACIONAL valor
                    | valor OP_RELACIONAL ID'''
    p[0] = p[1]

def p_for_step(p):
    '''for_step : ID OP_SINGLE_DECREMENT
                | ID OP_SINGLE_INCREMENT
                | ID OP_DECREMENT valor
                | ID OP_INCREMENT valor'''

# --- Sofia Izaguirre ---
def p_de_map(p):
    '''de_map : '''

# --- Daniel Cortez ---
def p_de_set(p):
    '''de_set : '''

# --- Alexander Nieves ---
def p_de_list(p):
    '''de_list : DT_LIST ID OP_ASSIGN DEL_LBRACKET list_content DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST ID OP_ASSIGN DEL_LBRACKET DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACKET list_content DEL_RBRACKET DEL_SEMICOLON
                | DT_LIST OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACKET DEL_RBRACKET DEL_SEMICOLON'''
    global log
    if p[2] == '<':
        message = f"Declaracion de estructura: List '{p[5]}'"
    else:
        message = f"Declaracion de estructura: List '{p[2]}'"
    log += message + '\n'
    p[0] = p[1]

def p_list_content(p):
    '''list_content : valor
                    | list_content DEL_COMMA valor'''
    p[0] = p[1]

# --- Sofia Izaguirre ---
# Declaracion de funcion estandar con retorno

# --- Daniel Cortez ---
# Funcion lambda/flecha

# --- Alexander Nieves ---
def p_fd_void(p):
    '''fd_void : KW_VOID ID DEL_LPAREN parameters DEL_RPAREN DEL_LBRACE body DEL_RBRACE'''
    global log
    message = f"Declaracion de funcion: Void '{p[2]}'"
    log += message + '\n'
    p[0] = p[1]

def p_parameters(p):
    '''parameters : parameter
                  | parameters DEL_COMMA parameter
                  | empty'''
    p[0] = p[1]

def p_parameter(p):
    '''parameter : data_type ID
                 | data_type OP_NULLABLE ID'''
    p[0] = p[1]

def p_body(p):
    '''body : instruction
            | body instruction
            | empty'''
    p[0] = p[1]

def p_empty(p):
    '''empty : '''
    pass

# --- Alexander Nieves ---
def p_data_type(p):
    '''data_type : DT_INT
                 | DT_DOUBLE
                 | DT_BOOL
                 | DT_STRING
                 | DT_LIST
                 | DT_MAP
                 | DT_SET
                 | KW_VAR'''
    p[0] = p[1]

def p_valor(p):
    '''valor : VAL_INT
             | VAL_DOUBLE
             | VAL_BOOL
             | VAL_STRING
             | KW_NULL'''
    p[0] = p[1]

def p_error(p):
    global log
    if p:
        message = f"Error Sintactico: Estructura no valida cerca de '{p.value}' en la linea {p.lineno}"
    else:
        message = "Error Sintactico: Fin de archivo inesperado (falta cerrar algo)"
    log += message + '\n'

parser = yacc.yacc()

def syntactic_analysis(lexer) -> str:
    global log

    log = ''
    parser.parse(lexer=lexer)
    response = log
    log = ''

    return response