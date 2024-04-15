import os
from tokenizer import MyTokenizer

def main():
    f = open("/home/ziad/Documents/faculty/8th-semester/compiler_design/repo/compiler/test_program.z", 'r')

    file_string = f.read()
    
    tokenizer = MyTokenizer()
    print(tokenizer.tokenize(file_string))

if __name__ == '__main__':
    main()
