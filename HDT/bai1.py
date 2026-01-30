class Numbers(object):
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def input(self):
        number1 = int(input())
        number2 = int(input())
        self.number1 = number1
        self.number2 = number2
    def printinfo(self):
        print(self.number1)
        print(self.number2)
    def addition(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multi(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 / self.number2
c = Numbers(0,0)
c.input()
c.printinfo()
print(c.addition())
print(c.subtract())
print(c.multi())
print(c.division())
        