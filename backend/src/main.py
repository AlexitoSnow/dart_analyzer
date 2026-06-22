from analyzer import analyzer
from file.write import write_lexical_log, write_syntactic_log
from file.read import read_file

import sys

print("Dart Analyzer")

try:
    author = int(sys.argv[1])
    filename = sys.argv[2]
    code = read_file(filename)
    analyzer.execute_analysis(author, code)
except Exception as e:
    sys.stderr.write(str(e) + '\n')