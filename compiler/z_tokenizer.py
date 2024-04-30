import re

class ZTokenizer:

    _keywords = ['if', 'let', 'int', 'string']
    _symbols = ['{', '}', '(', ')',';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '==', '>=', '<=']
    _op = ['+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '==', '>=', '<=']
    _token = ''

    def __init__(self, program):
        self._cursor = 0
        self._program = program


    # extracting the next token
    def get_next_token(self):
        if (not self.has_more_tokens()):
            return None

        self._token = ''

        # first: clearning white spaces
        while self.is_whitespace():
            self._cursor+=1
            if not self.has_more_tokens():
                return None

        # second: handling symbols
        if self._program[self._cursor] in self._symbols:
            if (self._program[self._cursor] in ['>', '<', '!', '='] and self._program[self._cursor+1] == '='):
                operator = self._program[self._cursor:self._cursor+2]
                self._token = operator
                self._cursor+=2
            else:
                self._token = self._program[self._cursor]
                self._cursor+=1


        # third: handling strings
        elif self._program[self._cursor] == '"':
            self._cursor+=1
            self._token = '"'

            while (self.has_more_tokens()):

                current_char = self._program[self._cursor]
                self._token = self._token + current_char
                self._cursor+=1
                if current_char == '"':
                    break

        # fourth: handling alphanumeric
        else:
            while self.has_more_tokens() and not self._program[self._cursor] in self._symbols\
            and not self.is_whitespace() and not self._program[self._cursor] == '"':
                
                current_char = self._program[self._cursor]
                self._token = self._token + current_char
                self._cursor+=1

        type = self.token_type(self._token)
        return (type, self._token)

    # returning the type of token
    def token_type(self, token):
        integer_pattern = re.compile("^[0-9]+$")
        identifier_pattern = re.compile("^[A-Za-z_][A-Za-z0-9_]*$")
        
        if token[0] == '"' and token[-1] == '"':
            return 'string'
        elif token in self._op:
            return 'operator'
        elif token in self._symbols:
            return 'symbol'
        elif integer_pattern.match(token):
            return 'integer'
        elif token in self._keywords:
            return 'keyword'
        elif identifier_pattern.match(token):
            return 'identifier'
        else:
            raise Exception('Lexical Error!')


    # checking for the end of the file
    def has_more_tokens(self):
        return self._cursor < len(self._program)

    # checking for white spaces
    def is_whitespace(self):
        if self._program[self._cursor] == ' ' or self._program[self._cursor] == '\n':
                return True
        return False