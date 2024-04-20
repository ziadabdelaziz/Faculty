from z_tokenizer import ZTokenizer

def main():
    f = open("tests/test1.z", 'r')

    file_string = f.read()
    
    tokenizer = ZTokenizer(file_string)
    token = None
    while True:
        token = tokenizer.get_next_token()
        if token == None:
            break
        print(token)

if __name__ == '__main__':
    main()
