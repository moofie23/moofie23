import math

class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        i = 0
        self.x = 0
        while i != 10:
            b = float(input('Введите число'))
            if b % 1 != 0:
                self.x = self.x + b
            else:
                self.x = self.x
            i = i + 1 
        return self.x
               
calculator = calc(0)

print(calculator.calcc())
