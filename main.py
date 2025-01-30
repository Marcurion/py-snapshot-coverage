class SystemUnderTest:
    def __init__(self, name):
        self.name = name

    def add(self, a: int, b: int):
        return a + b

    def sub(self, a:int, b:int):
        return a - b

    def concat(self, a:str, b:int):
        return f'{a} + {b} = {a + str(b)}'