class Dagiac(object):
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.h = h
class Hinhbinhhanh(Dagiac):
    def chuvi(self):
        return (self.x+self.y)*2
    def dientich(self):
        return (self.y*self.h)
class Hinhchunhat(Hinhbinhhanh):
    def chuvi(self):
        return (self.x+self.y)*2
    def dientich(self):
        return (self.x*self.y)
class Hinhvuong(Hinhchunhat):
    def chuvi(self):
        return self.x*4
    def dientich(self):
        return (self.x*self.x)
chon = int(0)
print("////Nhap hinh muon tinh////")
print("////1.Hinh binh hanh   ///")
print("////2.Hinh chu nhat   ///")
print("////3.Hinh vuong   ///")
print("Vui long nhap: ", end ="")
chon = int(input())
if chon == 1:
    print("Nhap chieu rong: ", end="")
    chieurong = int(input())
    print("Nhap chieu dai: ", end="")
    chieudai = int(input())
    print("Nhap chieu cao: ", end="")
    chieucao = int(input())
    c = Hinhbinhhanh(chieurong,chieudai,chieucao)
    print("Chu vi la:")
    print(c.chuvi())
    print("Dien tich la:")
    print(c.dientich())
elif chon == 2:
    print("Nhap chieu rong: ", end="")
    chieurong = int(input())
    print("Nhap chieu dai: ", end="")
    chieudai = int(input())
    c = Hinhchunhat(chieurong,chieudai,0)
    print("Chu vi la:")
    print(c.chuvi())
    print("Dien tich la:")
    print(c.dientich())
elif chon == 3:
    print("Nhap canh: ", end="")
    chieurong = int(input())
    c = Hinhvuong(chieurong,0,0)
    print("Chu vi la:")
    print(c.chuvi())
    print("Dien tich la:")
    print(c.dientich())
    
