hocphan = {
    "mahp":"",
    "ten":"",
    "sotc":0,
}
danhsach = []
n = int(input())
for i in range(n):
  a = hocphan.copy()
  mhp = input()
  ten=input()
  sotc = int(input())
  a["mahp"] = mhp
  a["ten"] = ten
  a["sotc"] = sotc
  danhsach.append(a)
print("danh sach can xem: ")
x = int(input())
print(danhsach[x-1]["mahp"])
print("tim hoc phan cntt")
for i in range(n):
    chuoicantim = danhsach[i]["mahp"]
    m = chuoicantim.find("TIN")
    if m==0:
        print(danhsach[i])