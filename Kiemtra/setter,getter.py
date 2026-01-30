class className:

    # Thuộc tính name
    name = ''
    so =int()

    # Setter cho name
    def setName(self, name):
        self.name = name
    def setSo(self,so):
        self.so = so

    # Getter cho name
    def getName(self):
        return self.name
    def getSo(self):
        return self.so
    def print(self):
        print(self.name)
    def printso(self):
        print(self.so)

# Sử dụng
c = className()
c.setName("Cường")
c.setSo(30)
print(c.getName())
print(c.getSo())
c.print()
c.printso()
# Kết quả: Cường