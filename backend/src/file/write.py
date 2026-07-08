from datetime import datetime
import os

authors = ['AlexanderNieves', 'SofiaIzaguirre', 'DanielCortez']

def write_lexical_log(author: int, data: str) -> None:
    write_log(author, data, 'lexico')

def write_syntactic_log(author: int, data: str) -> None:
    write_log(author, data, 'sintactico')

def write_semantic_log(author: int, data: str) -> None:
    write_log(author, data, 'semantico')
    
def write_log(author: int, data: str, type: str) -> None:
    if author > len(authors) - 1 or author < 0:
        raise IndexError("Author not found")
    
    instant = datetime.now().strftime("%d-%m-%Y-%Hh%Mm%Ss")

    path = os.path.join("logs", f'{type}-{authors[author]}-{instant}.txt')

    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    with open(path, "a") as f:
        print(f'Writing {type} analysis log at {path}')
        f.write(data + "\n")
        print(f'{type} analysis log written successfully!')