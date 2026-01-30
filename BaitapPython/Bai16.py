##Nhap dong du lieu chua day gia tri tu ban phim
dayGiaTri = input()
##Su dung ham split() de cat day gia tri thanh cac chuoi con
danhSachGiaTri = dayGiaTri.split(",")
n=len(danhSachGiaTri)
a=0
for i in range(0,n):
    s = danhSachGiaTri[i]
    sum = (int(s[0])*2**3)+(int(s[1])*2**2)+(int(s[2])*2**1)+(int(s[3])*2**0)
    if sum%5==0:
        a+=1
        if a==1:
          print(danhSachGiaTri[i],end="")   
        else:
          print(",",end="")
          print(danhSachGiaTri[i],end="")
        