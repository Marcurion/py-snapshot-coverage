class SystemUnderTest:
    def __init__(self, name):
        self.name = name

    def add(self, a: int, b: int):
        return a + b

    def sub(self, a:int, b:int):
        return a - b

    def concat(self, a:str, b:int):
        return f'{a} + {b} = {a + str(b)}'

    def mean(self, a:int, b:int, c:int, d:int):
        return (a + b + c + d) / 4

    def concat(self, *args):
        output = ""
        for arg in args:
            output += str(arg)
        return output