import math

class calc:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def cal(self):
        y = math.sqrt((self.z + self.x)**2 - self.x**2)
        print(y)
        
calculator = calc(6350, 200)

calculator.cal()
