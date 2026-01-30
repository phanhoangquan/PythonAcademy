class className:
 
    # Thuộc tính name
    __name = ''
 
    # Setter cho name
    def setName(self, name):
        self.__name = name
 
    # Getter cho name
    def getName(self):
        return self.__name
 
# Sử dụng
c = className()
c.setName("Cường")
print(c.getName())
# Kết quả: Cường