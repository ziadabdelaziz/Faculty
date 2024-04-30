from z_tokenizer import ZTokenizer
from z_parser import ZParserBeta

class ZAnalyzer:
    def __init__(self, file_text, symbol_table):
        self._tokenizer = ZTokenizer(file_text)
        self._parser = ZParserBeta(file_text, symbol_table)

    def analyze(self):
        self._parser.parse_statements()
