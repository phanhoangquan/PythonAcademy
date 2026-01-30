import array as arr 
class SV(object):
    def __init__(self,lop,hoten):
        self.lop = lop
        self.hoten = hoten
    def show(self):
        print("Lop: ",self.lop)
        print("Ho ten: ",self.hoten)
class SVIT(SV):
    def __init__(self,lop,hoten,dtb,hocbong):
        SV.__init__(self,lop,hoten)
        self.dtb = dtb
        self.hocbong = hocbong
    def show2(self):
        SV.show(self)
        print("Diem trung binh: ",self.dtb)
        print("Hoc bong: ",self.hocbong)
class SVCN(SV):
    def __init__(self, lop, hoten,dtb,hocbong,hocphi):
        SVIT.__init__(self, lop, hoten,dtb,hocbong)
        self.hocphi=hocphi
    def show3(self):
        SVIT.show2(self)
        print("Hoc phi cua sinh vien cu nhan:",self.hocphi)
##DEF
def Cau1abc():
    a=input()
    b=input()
    s1=SV(a,b)
    s1.show()
    c=float(input())
    d=int(input())
    s2=SVIT(a,b,c,d)
    s2.show2()
    e=int(input())
    s3=SVCN(a,b,c,d,e)
    s3.show3()
def Cau1d():
    print("Nhap so sv: ")
    n = int(input())
    list=[]
    for i in range(n):
        a=input()
        b=input()
        c=float(input())
        d=int(input())
        e=int(input())
        x = [a,b,c,d,e]
        list.append(x)
    print("thong tin sinh vien so:")
    m = int(input())
    sv1 = SVCN(list[m-1][0],list[m-1][1],list[m-1][2],list[m-1][3],list[m-1][4])
    sv1.show3()

##Main
Cau1abc()
Cau1d()