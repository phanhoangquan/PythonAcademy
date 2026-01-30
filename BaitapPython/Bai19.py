#Nhap dong du lieu chua day gia tri tu ban phim
dayGiaTri = input()
#Su dung ham split() de cat day gia tri thanh cac chuoi con
danhSachGiaTri = dayGiaTri.split(",")
n=len(danhSachGiaTri)
for i in range(n):
    if int(danhSachGiaTri[i])%2!=0:
        if i < n-1:
            print(danhSachGiaTri[i], end=",")
        else:
             print(danhSachGiaTri[i])
