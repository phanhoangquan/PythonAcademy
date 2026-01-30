from fractions import Fraction
from decimal import Decimal
class phanso(object):
    def __init__(self,tu,mau,tu2,mau2):
        self.tu = tu
        self.mau = mau
        self.tu2 = tu2
        self.mau2 = mau2
    def nhapps1(self):
        print("//NHAP PHAN SO THU 1//")
        print("Nhap tu so: ", end ="")
        tu = int(input())
        print("Nhap mau so: ", end ="")
        mau = int(input())
        self.tu = tu
        self.mau = mau
    def nhapps2(self):
        print("//NHAP PHAN SO THU 2//")
        print("Nhap tu so: ", end ="")
        tu2 = int(input())
        print("Nhap mau so: ", end ="")
        mau2 = int(input())
        self.tu2 = tu2
        self.mau2 = mau2
    def inps1(self):
        if self.mau != 0:
          print("Phan so thu 1 la: ", self.tu,"/",self.mau)
        elif self.mau == 0:
          print("Day khong phai la phan so")
        elif self.tu == 0:
          print("Phan so thu 1 la: 0")
    def inps2(self):
        if self.mau2 != 0:
          print("Phan so thu 2 la: ", self.tu2,"/",self.mau2)
        elif self.tu2 == 0 and self.mau2 == 0:
          print("Day khong phai la phan so")
        elif self.tu2 == 0:
          print("Phan so thu 2 la: 0")
    def rutgonps1(self):
        print("Rut gon cua phan so thu 1 la: ")
        print(Fraction(self.tu,self.mau))
    def rutgonps2(self):
        print("Rut gon cua phan so thu 1 la: ")
        print(Fraction(self.tu2,self.mau2))
    def add(self):
        pstu = (self.tu*self.mau2) + (self.mau*self.tu2)
        psmau = (self.mau*self.mau2)
        print("Cong hai phan so: ", pstu,"/",psmau)
    def sub(self):
        pstu = (self.tu*self.mau2) - (self.mau*self.tu2)
        psmau = self.mau*self.mau2
        print("Tru hai phan so: ", pstu,"/",psmau)
    def mul(self):
        pstu = self.tu * self.tu2
        psmau = self.mau * self.mau2
        print("Nhan hai phan so: ", pstu,"/",psmau)
    def div(self):
        pstu = self.tu * self.mau2
        psmau = self.mau * self.mau2
        print("Chia hai phan so: ", pstu,"/",psmau)

a = phanso(0,0,0,0)
a.nhapps1()
a.nhapps2()
a.inps1()
a.inps2()
a.rutgonps1()
a.rutgonps2()
a.add()
a.sub()
a.mul()
a.div()
