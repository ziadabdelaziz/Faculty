from z_tokenizer import ZTokenizer

class ZParser:
    _indentation = 0

    def __init__(self, program):
        self._tokenizer = ZTokenizer(program)
        return

    def parse_statements(self):
        print('statements:')

        token = self._tokenizer.get_next_token()
        self._indentation+=1

        while token:
            if token[1] in ['bool', 'int', 'string']:
                self.parse_dec_statement(token)
            elif token[1] == 'let':
                self.parse_let_statement()
            elif token[1] == 'if':
                self.parse_if_statement()

            token = self._tokenizer.get_next_token()

        self._indentation-=1

        return

    def parse_dec_statement(self, terminal):
        print('\t'*self._indentation, 'dec_statement:')

        self._indentation+=1
        print('\t'*self._indentation, terminal[0]+':', terminal[1])

        token = self._tokenizer.get_next_token()

        if token[0] == 'identifier':
            print('\t'*self._indentation, token[0]+':', token[1])

        token = self._tokenizer.get_next_token()
        if token[1] == '=':
            print(token)
            print('\t'*self._indentation, 'op:', token[1])
            self.parse_expresion()
            token = self._tokenizer.get_next_token()

        if token[1] == ';':
            print('\t'*self._indentation, token[0]+':', token[1])

        self._indentation-=1

        return

    def parse_if_statement(self):
        print('\t'*self._indentation, 'if_statement:')

        self._indentation+=1
        print('\t'*self._indentation, 'keyword:', 'if')

        token = self._tokenizer.get_next_token()
        if token[1] == '(':
            print('\t'*self._indentation, token[0]+':', token[1])
            self.parse_expresion()
        else:
            raise Exception('Syntax Error!')

        token = self._tokenizer.get_next_token()
        if token[1] in ['==', '>=', '<=', '>', '<']:
            print('\t'*self._indentation, token[0]+':', token[1])
            self.parse_expresion()
        elif token[0] in ['identifier', 'integer', 'string']:
            print('\t'*self._indentation, 'expression:')
            self.parse_term(token) 
            self._indentation+=1
        else:
            raise Exception('Syntax Error!')

        token = self._tokenizer.get_next_token()
        if token[1] == ')':
            print('\t'*self._indentation, token[0]+':', token[1])
        else:
            raise Exception('Syntax Error!')

        token = self._tokenizer.get_next_token()
        if token[1] == '{':
            print('\t'*self._indentation, token[0]+':', token[1])
            self.parse_statements()
        else:
            raise Exception('Syntax Error!')
        
        token = self._tokenizer.get_next_token()
        if token[1] == '}':
            print('\t'*self._indentation, token[0]+':', token[1])
        else:
            raise Exception('Syntax Error!')

        self._indentation-=1
        return

    def parse_let_statement(self):
        print('\t'*self._indentation, 'let_statement:')

        self._indentation+=1
        print('\t'*self._indentation, 'keyword:', 'let')

        token = self._tokenizer.get_next_token()

        if token[0] == 'identifier':
            print('\t'*self._indentation, token[0]+':', token[1])

        token = self._tokenizer.get_next_token()
        if token[1] == '=':
            print('\t'*self._indentation, 'op:', token[1])
            self.parse_expresion()
            token = self._tokenizer.get_next_token()

        
        if token[1] == ';':
            print('\t'*self._indentation, token[0]+':', token[1])

        self._indentation-=1

        return


    def parse_expresion(self):
        print('\t'*self._indentation, 'expression:')

        token = self._tokenizer.get_next_token()
        self._indentation+=1

        if token[0] in ['identifier', 'integer', 'string']:
            self.parse_term(token)

        self._indentation-=1

        return


    def parse_term(self, terminal):
        print('\t'*self._indentation, 'term:')
        self._indentation+=1

        print('\t'*self._indentation, terminal[0]+':', terminal[1])

        self._indentation-=1
        
        return
