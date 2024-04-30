from z_tokenizer import ZTokenizer
from z_parser_beta import ZParserBeta

class ZAnalyzer:
    def __init__(self, file_text):
        self._tokenizer = ZTokenizer(file_text)
        self._parser = ZParserBeta(file_text)
    
    def analyze(self):
        self._parser.parse_statements()

