import re

class MyTokenizer :

    def __init__(self):
        return

    # Define token types using regular expressions
    _token_specification = [
        ('KEYWORD',   r'\b(if|else|for|while)\b'),      # keywords reserved for the language
        ('DATATYPE',  r'\b(int|bool|double|string)\b'), # data types
        ('NUMBER',    r'\d+(\.\d*)?'),                  # Integer or decimal number
        ('ID',        r'[a-zA-Z_]\w*'),                 # Identifier
        ('OP',        r'\=\=|\+|\-|\*|\=|\>|\<'),       # operators
        ('SYMBOL',    r'\(|\)|\;'),                     # symbols
        ('NEWLINE',   r'\n'),                           # Line ending
        ('SKIP',      r'[ \t]+'),                       # Skip over spaces and tabs
    ]

    # Combine all the regular expressions into a single pattern
    _token_regex = '|'.join('(?P<%s>%s)' % pair for pair in _token_specification)

    def tokenize(self, code):
        tokens = []
        for mo in re.finditer(self._token_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind != 'SKIP' and kind != 'NEWLINE':
                tokens.append((kind, value))
        return tokens
