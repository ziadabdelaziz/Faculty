from z_tokenizer import ZTokenizer
from z_parser import ZParser
from z_analyzer import ZAnalyzer

def main():
    f = open("tests/test4.z", 'r')

    file_string = f.read()

    analyzer = ZAnalyzer(file_string)
    analyzer.analyze()

if __name__ == '__main__':
    main()
