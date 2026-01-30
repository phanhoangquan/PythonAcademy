class nhanvien(object):
    def __init__(self,ten,tuoi,diachi,tienluong,tongsogiolam):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.tongsogiolam = tongsogiolam
    def inputinfo(self):
        print("Nhap ten: ",end="")
        ten = input()
        print("Nhap tuoi: ",end="")
        tuoi = int(input())
        print("Nhap dia chi: ",end="")
        diachi = input()
        print("Nhap tien luong: ",end="")
        tienluong = int(input())
        print("Nhap tongsogiolam: ",end="")
        tongsogiolam = int(input())
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.tongsogiolam = tongsogiolam
    def printinfo(self):
        print("//////THONG TIN NHAN VIEN/////")
        print("Ten: ", end="")
        print(self.ten)
        print("Tuoi: ", end="")
        print(self.tuoi)
        print("Dia chi: ", end="")
        print(self.diachi)
        print("Tien luong: ", end="")
        print(self.tienluong)
        print("So gio lam: ", end="")
        print(self.tongsogiolam)
    def tinhthuong(self):
        if self.tongsogiolam >=200:
            tienthuong = self.tienluong * 0.2
            print("So luong thuong: %d " %(tienthuong))
        elif 100<=self.tongsogiolam<200:
            tienthuong = self.tienluong * 0.1
            print("So luong thuong: %d " %(tienthuong))
        elif self.tongsogiolam<100:
            tienthuong = 0
            print("So luong thuong: %d " %(tienthuong))
c = nhanvien("",0,"",0,0)
c.inputinfo()
c.printinfo()
c.tinhthuong()