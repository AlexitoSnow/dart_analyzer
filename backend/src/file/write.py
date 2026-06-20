from datetime import datetime
import os

authors = ['AlexanderNieves', 'SofiaIzaguirre', 'DanielCortez']

def write_log(author: int, data: dict) -> None:
    if author > len(authors) - 1 or author < 0:
        raise IndexError("Author not found")
    
    instant = datetime.now().strftime("%d-%m-%Y-%Hh%Mm%Ss")

    path = os.path.join("logs", f'lexico-{authors[author]}-{instant}.txt')

    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    with open(path, "a") as f:
        print(f'Writing output at {path}')
        f.write(str(data) + "\n")
        print('Output written successfully!')

    