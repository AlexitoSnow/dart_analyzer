import sys
import os
import ply.lex as lex

# Ensure the 'src' folder is in Python's import path
src_dir = os.path.dirname(os.path.abspath(__file__))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from analyzer import lexical
from analyzer.lexical import lexical_analysis
from analyzer.syntactic import syntactic_analysis
from analyzer.semantic import semantic_analysis
from file.read import read_file
from file.write import write_lexical_log, write_syntactic_log, write_semantic_log

def parse_args():
    """Parses command line arguments and returns mode, author_idx, and filename."""
    if len(sys.argv) < 4:
        sys.stderr.write("Error: Uso: python gui_bridge.py <mode> <author_idx> <filename>\n")
        sys.exit(1)
        
    mode = sys.argv[1]
    
    try:
        author_idx = int(sys.argv[2])
    except ValueError:
        sys.stderr.write("Error: El índice del autor debe ser un número entero (0, 1, 2).\n")
        sys.exit(1)
        
    filename = sys.argv[3]
    if filename.endswith('.dart'):
        filename = filename[:-5]
        
    return mode, author_idx, filename

def read_dart_code(filename):
    """Reads Dart code from the algorithms directory using the backend's read_file module."""
    try:
        return read_file(filename)
    except Exception as e:
        sys.stderr.write(f"Error al leer el archivo '{filename}': {str(e)}\n")
        sys.exit(1)

def execute_lexical_pass(code, author_idx):
    """Executes lexical analysis, writes logs, and reports errors if found."""
    lexer = lex.lex(module=lexical)
    lexer.lineno = 1
    lexer.input(code)
    try:
        result = lexical_analysis(lexer)
        write_lexical_log(author_idx, result)
        if "Caracter ilegal" in result:
            sys.stderr.write(result)
            sys.exit(1)
        else:
            sys.stdout.write(result)
            sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error en Análisis Léxico: {str(e)}\n")
        sys.exit(1)

def execute_syntactic_pass(code, author_idx):
    """Executes syntactic analysis, writes logs, and reports errors if found."""
    lexer = lex.lex(module=lexical)
    lexer.lineno = 1
    lexer.input(code)
    try:
        result = syntactic_analysis(lexer)
        write_syntactic_log(author_idx, result)
        if "Error Sintactico" in result:
            sys.stderr.write(result)
            sys.exit(1)
        else:
            sys.stdout.write(result)
            sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error en Análisis Sintáctico: {str(e)}\n")
        sys.exit(1)

def execute_semantic_pass(code, author_idx):
    """Executes semantic analysis, resets module depth state, writes logs, and reports errors if found."""
    lexer = lex.lex(module=lexical)
    lexer.lineno = 1
    lexer.input(code)
    try:
        from analyzer import semantic
        semantic.loop_and_switch_depth = 0
        
        result = semantic_analysis(lexer)
        write_semantic_log(author_idx, result)
        if "Error Semántico" in result or "Error Semantico" in result:
            sys.stderr.write(result)
            sys.exit(1)
        else:
            sys.stdout.write(result)
            sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error en Análisis Semántico: {str(e)}\n")
        sys.exit(1)

def main():
    mode, author_idx, filename = parse_args()
    code = read_dart_code(filename)
    
    if mode == 'lexico':
        execute_lexical_pass(code, author_idx)
    elif mode == 'sintactico':
        execute_syntactic_pass(code, author_idx)
    elif mode == 'semantico':
        execute_semantic_pass(code, author_idx)
    else:
        sys.stderr.write(f"Modo desconocido: {mode}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
