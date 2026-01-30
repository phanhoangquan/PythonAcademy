hanghoa = {
    "Ten":"",
    "SoLuong":0,
    "GiaBan":0
}
danhsach = []
n=int(0)
for i in range(999):
    print("Nhap vao hang hoa thu",i+1)
    a = hanghoa.copy()
    print("Nhap ten:",end="")
    Ten = input()
    if Ten =="":
        break
    print("Nhap so luong:",end="")
    SoLuong = int(input())
    print("Nhap gia ban:",end="")
    GiaBan = int(input())
    a["Ten"]=Ten
    a["SoLuong"]=SoLuong
    a["GiaBan"]=GiaBan
    danhsach.append(a)
    n=n+1
##in ra mat hang so luong con duoi 5
print("Nhung mat hang so luong con duoi 5 la: ")
for i in range(n):
    if(danhsach[i]["SoLuong"]<5):
        print(danhsach[i])
##in tong so tien hang
print("Tong so tien hang la: ")
tienhang = int(0)
for i in range(n):
    tienhang = tienhang + (danhsach[i]["SoLuong"]*danhsach[i]["GiaBan"])
print(tienhang)