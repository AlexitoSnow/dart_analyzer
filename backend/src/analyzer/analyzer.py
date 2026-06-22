import ply.lex as lex

from . import lexical
from .lexical import lexical_analysis
from .syntactic import syntactic_analysis
from file.write import write_lexical_log, write_syntactic_log


def execute_analysis(author: int, code: str) -> None:
    lexer = lex.lex(module=lexical)
    
    lexer.lineno = 1
    lexer.input(code)
    
    lexical_log = lexical_analysis(lexer)
    write_lexical_log(author, lexical_log)

    lexer.lineno = 1
    lexer.input(code)
    
    syntactic_log = syntactic_analysis(lexer)
    write_syntactic_log(author, syntactic_log)