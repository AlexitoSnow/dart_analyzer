import ply.lex as lex

tokens = ('ID', 'DELIMITER', 'COMMENT')
log = ''

t_DELIMITER = r'[\(\);]\w*'
t_ID = r'[a-zA-Z_]\w*'

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
