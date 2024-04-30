from z_tokenizer import ZTokenizer
from z_symbol_table import ZSymbolTable


class ZParserBeta:
    _indentation = 0
    _current_token = ''
    _previous = False
    _symbol_table = ZSymbolTable()

    def __init__(self, program, symbol_table):
        self._tokenizer = ZTokenizer(program)
        self._symbol_table = symbol_table
        return


    def parse_statements(self):
        self._current_token = self._tokenizer.get_next_token()
        if self._current_token == None:
            return

        if self._current_token[1] == '}':
            self._previous = True
            return

        print('\t'*self._indentation+'statements:')
        self._indentation+=1

        if self._current_token[1] in ['int', 'string']:
            self.parse_dec_statement(self._current_token)
        elif self._current_token[1] == 'let':
            self.parse_let_statement()
        elif self._current_token[1] == 'if':
            self.parse_if_statement()
        else:
            raise Exception('undefined statement')

        self._indentation-=1
        self.parse_statements()


    def parse_dec_statement(self, type):
        print('\t'*self._indentation+'dec_statement:')
        self._indentation+=1

        print('\t'*self._indentation+type[0]+':', type[1])

        self.expect('identifier', 0)
        self._symbol_table.insert(self._current_token[1], type[1])
        self.expect('=', 1)
        self.parse_expression()
        self.expect(';', 1)

        self._indentation-=1


    def parse_if_statement(self):
        print('\t'*self._indentation+'if_statement:')
        self._indentation+=1

        print('\t'*self._indentation+self._current_token[0]+':', self._current_token[1])

        self.expect('(', 1)
        self.parse_expression()
        self.expect(')', 1)
        self.expect('{', 1)
        self.parse_statements()
        self.expect('}', 1)

        self._indentation-=1


    def parse_let_statement(self):
        print('\t'*self._indentation+'let_statement:')
        self._indentation+=1

        print('\t'*self._indentation+self._current_token[0]+':', self._current_token[1])

        self.expect('identifier', 0)

        if self._symbol_table.lookup(self._current_token) == None:
            error_statement = '"'+self._current_token[1]+'"'+' is not defined'
            raise Exception(error_statement)

        self.expect('=', 1)
        self.parse_expression()
        self.expect(';', 1)

        self._indentation-=1


    def parse_expression(self):
        print('\t'*self._indentation, 'expression')
        self._indentation+=1

        self.parse_term()

        self._indentation-=1


    def parse_term(self):
        print('\t'*self._indentation, 'term')
        self._indentation+=1
        self.expect(['identifier', 'integer', 'string'], 0)
        try:
            self.expect('operator', 0)
            self.parse_term()
        except:
            self._previous = True
    
        self._indentation-=1


    def expect(self, token, index):
        if not self._previous:
            self._current_token = self._tokenizer.get_next_token()
        else:
            self._previous = False

        # if we are expecting different possibilities
        if isinstance(token, list):
            if self._current_token[index] in token:
                print('\t'*self._indentation, self._current_token[0], ':', self._current_token[1])
            else:
                error_statement = 'expected term of type' ,token,'but found', self._current_token
                raise Exception(error_statement)

        # if we are expecting one possibility
        elif self._current_token[index] == token:
            print('\t'*self._indentation, self._current_token[0], ':', self._current_token[1])
        else:
            error_statement = 'expected', token, 'of type' ,self._tokenizer.token_type(token),'but found', self._current_token
            raise Exception(error_statement)
