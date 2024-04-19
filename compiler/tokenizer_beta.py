class TokenizerBeta:

    def __init__(self, program):
        self._cursor = 0
        self._program = program

    def has_more_tokens(self):
        return self._cursor < len(self._program)
    
    def get_next_token(self):
        if (not self.has_more_tokens()):
            return None
        
        text = self._program[self._cursor:]
