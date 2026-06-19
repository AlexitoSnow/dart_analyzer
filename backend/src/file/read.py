import os

def read_file(filename: str) -> str:
    path = os.path.join('algorithms', f'{filename}.dart')

    if not os.path.exists(path):
        raise FileNotFoundError(f'File not found at {path}')

    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        raise Exception(str(e))