import math
class Iris(object):
    kieuhoa = ""
    def __init__(self,x1,x2,x3,x4,kieuhoa):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.kieuhoa = kieuhoa
    def setKieuhoa(self,kieuhoa):
        self.kieuhoa = kieuhoa
class IrisK(Iris):
    def __init__(self, x1, x2, x3, x4, kieuhoa,kx1,kx2,kx3,kx4,kkieuhoa):
        Iris.__init__(self,x1,x2,x3,x4,kieuhoa)
        self.kx1 = kx1
        self.kx2 = kx2
        self.kx3 = kx3
        self.kx4 = kx4
        self.kkieuhoa = kkieuhoa
    def tinhKhoangCach(self):
      khoang_cach = math.sqrt(
      (self.x1 - self.kx1) ** 2 +
      (self.x2 - self.kx2) ** 2 +
      (self.x3 - self.kx3) ** 2 +
      (self.x4 - self.kx4) ** 2
      )
      return round(khoang_cach, 2)
##Main
print("///////////////NHAP THONG TIN CUA CAY IRIS H////////////////")
print("Nhap chieu dai dai hoa(cm):", end="")
x1 = int(input())
print("Nhap chieu rong dai hoa(cm):", end="")
x2 = int(input())
print("Nhap chieu dai canh hoa(cm):", end="")
x3 = int(input())
print("Nhap chieu rong canh hoa(cm):", end="")
x4 = int(input())
print("Nhap kieu hoa(de trong neu chua biet kieu hoa):",end="")
kieuhoa = input()
if(kieuhoa == ""):
    kieuhoa = "None"
c = Iris(x1,x2,x3,x4,kieuhoa)
print("Nhap kieu hoa (set ): ")
kieuhoaset = input()
c.setKieuhoa(kieuhoaset)
print("///////////////NHAP THONG TIN CUA CAY IRIS K////////////////")
print("Nhap chieu dai dai hoa(cm):", end="")
kx1 = int(input())
print("Nhap chieu rong dai hoa(cm):", end="")
kx2 = int(input())
print("Nhap chieu dai canh hoa(cm):", end="")
kx3 = int(input())
print("Nhap chieu rong canh hoa(cm):", end="")
kx4 = int(input())
print("Nhap kieu hoa:",end="")
kkieuhoa = input()
c2 = IrisK(x1,x2,x3,x4,kieuhoa,kx1,kx2,kx3,kx4,kkieuhoa)
print("///////////////KHOANG CACH HOA H VA K ////////////////")
print("Khoang cach la:",end="")
print(c2.tinhKhoangCach())


    
        