from analyzer.lexical import lexical_analysis
import sys
from file.write import write_log
from file.read import read_file

print("Dart Analyzer")

try:
    author = int(sys.argv[1])
    filename = sys.argv[2]
    code = read_file(filename)
    log = lexical_analysis(code)
    write_log(author, log)
except Exception as e:
    sys.stderr.write(str(e) + '\n')