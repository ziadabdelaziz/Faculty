import sys
from z_analyzer import ZAnalyzer

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

    analyzer = ZAnalyzer(file_string)
    analyzer.analyze()

if __name__ == '__main__':
    main()
