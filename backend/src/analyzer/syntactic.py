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
                            | vd_nullability
                            | vd_inference
                            | vd_static'''
    p[0] = p[1]

def p_expressions(p):
    '''expressions : arithmetic_expression
                   | boolean_expression'''
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
    '''function_declarations : fd_void
                            | fd_return
                            | fd_lambda'''
    p[0] = p[1]

# --- Daniel Cortez ---
def p_input_output(p):
    '''input_output : io_print
                    | io_read'''
    p[0] = p[1]

# --- Alexander Nieves ---
def p_vd_inmutability(p):
    '''vd_inmutability : KW_FINAL ID OP_ASSIGN valor DEL_SEMICOLON
                       | KW_CONST ID OP_ASSIGN valor DEL_SEMICOLON'''
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
def p_vd_inference(p):
    '''vd_inference : KW_VAR ID OP_ASSIGN valor DEL_SEMICOLON
                    | KW_VAR ID OP_ASSIGN arithmetic_expression DEL_SEMICOLON'''
    global log
    log += f"Declaracion de variable: Inferencia de tipo '{p[2]}'\n"

# --- Daniel Cortez ---
# Declaracion de variable Forma 2 (Tipado Estático)
def p_vd_static(p):
    '''vd_static : data_type ID OP_ASSIGN valor DEL_SEMICOLON
                 | data_type ID DEL_SEMICOLON
                 | data_type ID OP_ASSIGN arithmetic_expression DEL_SEMICOLON'''
    global log
    log += f"Declaracion de variable: Tipado estatico '{p[2]}'\n"

# --- Alexander Nieves ---
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

# --- Sofia Izaguirre ---
# Expresiones booleanas
def p_boolean_expression(p):
    '''boolean_expression : valor OP_RELACIONAL valor
                          | boolean_expression OP_LOGIC boolean_expression
                          | KW_TRUE
                          | KW_FALSE'''
    p[0] = p[1]

# --- Sofia Izaguirre ---
def p_ce_if_else(p):
    '''ce_if_else : KW_IF DEL_LPAREN boolean_expression DEL_RPAREN DEL_LBRACE body DEL_RBRACE
                  | KW_IF DEL_LPAREN boolean_expression DEL_RPAREN DEL_LBRACE body DEL_RBRACE KW_ELSE DEL_LBRACE body DEL_RBRACE'''
    global log
    if len(p) == 8:
        log += "Estructura de control: IF\n"
    else:
        log += "Estructura de control: IF-ELSE\n"

# --- Daniel Cortez ---
def p_ce_while(p):
    '''ce_while : KW_WHILE DEL_LPAREN boolean_expression DEL_RPAREN DEL_LBRACE body DEL_RBRACE'''
    global log
    log += "Estructura de control: While\n"

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
    '''de_map : DT_MAP OP_LESS data_type DEL_COMMA data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACE map_elements DEL_RBRACE DEL_SEMICOLON
              | DT_MAP ID OP_ASSIGN DEL_LBRACE map_elements DEL_RBRACE DEL_SEMICOLON'''
    global log
    if len(p) == 13:
        log += f"Declaracion de estructura: Map '{p[7]}'\n"
    else:
        log += f"Declaracion de estructura: Map '{p[2]}'\n"

def p_map_elements(p):
    '''map_elements : valor DEL_COLON valor
                    | valor DEL_COLON valor DEL_COMMA map_elements
                    | empty'''
    pass

# --- Daniel Cortez ---
def p_de_set(p):
    '''de_set : DT_SET OP_LESS data_type OP_GREATHER ID OP_ASSIGN DEL_LBRACE set_elements DEL_RBRACE DEL_SEMICOLON
              | DT_SET ID OP_ASSIGN DEL_LBRACE set_elements DEL_RBRACE DEL_SEMICOLON'''
    global log
    if len(p) == 11:
        log += f"Declaracion de estructura: Set '{p[5]}'\n"
    else:
        log += f"Declaracion de estructura: Set '{p[2]}'\n"

def p_set_elements(p):
    '''set_elements : valor
                    | valor DEL_COMMA set_elements
                    | empty'''
    pass

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
def p_fd_return(p):
    '''fd_return : data_type ID DEL_LPAREN parameters DEL_RPAREN DEL_LBRACE body KW_RETURN valor DEL_SEMICOLON DEL_RBRACE
                 | data_type ID DEL_LPAREN parameters DEL_RPAREN DEL_LBRACE body KW_RETURN arithmetic_expression DEL_SEMICOLON DEL_RBRACE'''
    global log
    log += f"Declaracion de funcion: Retorno '{p[2]}'\n"

# --- Daniel Cortez ---
# Funcion lambda/flecha
def p_fd_lambda(p):
    '''fd_lambda : data_type ID DEL_LPAREN parameters DEL_RPAREN OP_FLECHA arithmetic_expression DEL_SEMICOLON
                 | data_type ID DEL_LPAREN parameters DEL_RPAREN OP_FLECHA boolean_expression DEL_SEMICOLON
                 | data_type ID DEL_LPAREN parameters DEL_RPAREN OP_FLECHA valor DEL_SEMICOLON'''
    global log
    log += f"Declaracion de funcion: Lambda '{p[2]}'\n"

# Impresión y Solicitud de datos
def p_io_print(p):
    '''io_print : KW_PRINT DEL_LPAREN print_content DEL_RPAREN DEL_SEMICOLON'''
    global log
    log += "Impresion de datos: print\n"

def p_print_content(p):
    '''print_content : valor
                     | ID
                     | valor OP_ARITHMETIC ID
                     | ID OP_ARITHMETIC ID'''
    pass

def p_io_read(p):
    '''io_read : data_type OP_NULLABLE ID OP_ASSIGN ID DEL_DOT ID DEL_LPAREN DEL_RPAREN DEL_SEMICOLON'''
    global log
    log += f"Solicitud de datos: readLineSync a la variable '{p[3]}'\n"


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
             | KW_NULL
             | ID'''
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