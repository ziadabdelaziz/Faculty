import sys
from z_analyzer import ZAnalyzer
from z_symbol_table import ZSymbolTable

def main():
    if len(sys.argv) != 2:
        print('you must provide one file name to compile')
        sys.exit(-1)

    filename = sys.argv[1]

    if filename[-2:] != '.z':
        print('your file must end with ".z"')
        sys.exit(-1)

    f = open(filename, 'r')

    file_string = f.read()

    symbol_table = ZSymbolTable()
    analyzer = ZAnalyzer(file_string, symbol_table)
    analyzer.analyze()

    print('=============================')
    print('The Symbol Table')
    print(symbol_table.table)

if __name__ == '__main__':
    main()
