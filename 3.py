class Calculator:
    def __init__(self,first=1,sec=1):
        self.first = first
        self.sec = sec
    def add(self):
        return self.first + self.sec
    def substract(self):
        return self.first - self.sec
    def multy(self):
        return self.first * self.sec
    def divide(self):
        return self.first / self.sec
calculator = Calculator(5,4)
print(calculator.add())
print(calculator.substract())
print(calculator.multy())
print(calculator.divide())