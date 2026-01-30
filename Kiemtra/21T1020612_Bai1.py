class SV(object):
    def __init__(self,lop,hoten):
        self.lop = lop
        self.hoten = hoten
    def nhap(self):
         print("Nhap lop: ")
         lop = input()
         print("Nhap ho ten: ")
         hoten = input()
         self.lop = lop
         self.hoten = hoten
    def xuat(self):
        print("THONG TIN SINH VIEN:")
        print(self.hoten)
        print(self.lop)
c = SV("","")
c.nhap()
c.xuat()




        