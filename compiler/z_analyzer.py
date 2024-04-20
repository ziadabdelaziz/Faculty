from z_tokenizer import ZTokenizer
from z_parser import ZParser

class ZAnalyzer:
    def __init__(self, file_text):
        self._tokenizer = ZTokenizer(file_text)
        self._parser = ZParser()
