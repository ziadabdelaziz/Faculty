class ZSymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, name, type):
        self.table[name] = type

    def lookup(self, name):
        return self.table.get(name, None)
