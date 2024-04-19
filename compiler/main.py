import os
from tokenizer import MyTokenizer

def main():
    f = open("tests/test1.z", 'r')

    file_string = f.read()
    
    tokenizer = MyTokenizer()
    print(tokenizer.tokenize(file_string))

if __name__ == '__main__':
    main()
