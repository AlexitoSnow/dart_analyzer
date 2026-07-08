import ply.lex as lex

from . import lexical
from .lexical import lexical_analysis
from .syntactic import syntactic_analysis
from .semantic import semantic_analysis  # <-- Importación estandarizada
from file.write import write_lexical_log, write_syntactic_log, write_semantic_log


def execute_analysis(author: int, code: str) -> None:
    lexer = lex.lex(module=lexical)
    
    # --- LÉXICO ---
    lexer.lineno = 1
    lexer.input(code)
    lexical_log = lexical_analysis(lexer)
    write_lexical_log(author, lexical_log)

    # --- SINTÁCTICO ---
    lexer.lineno = 1
    lexer.input(code)
    syntactic_log = syntactic_analysis(lexer)
    write_syntactic_log(author, syntactic_log)

    # --- SEMÁNTICO ---
    lexer.lineno = 1
    lexer.input(code)
    semantic_log = semantic_analysis(lexer)
    write_semantic_log(author, semantic_log)