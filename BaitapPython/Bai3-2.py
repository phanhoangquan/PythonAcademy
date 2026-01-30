import math
##Nhap dong du lieu chua day gia tri tu ban phim
dayGiaTri = input()
##Su dung ham split() de cat day gia tri thanh cac chuoi con
hocsinh = dayGiaTri.split(" ")
######## 1.So hoc sinh trong lop
print("Lop co so hoc sinh la: ", len(hocsinh),"hoc sinh")
######## 2.tinh chieu cao trung binh
chieucaotb = int(0)
for i in range(0,len(hocsinh)):
    chieucaotb = chieucaotb + int(hocsinh[i])
chieucaotb = chieucaotb / len(hocsinh)
print("Vay chieu cao trung binh cua cac hoc sinh trong lop la", chieucaotb)
########3.Liet ke chieu cao khac nhau]
# Chuyển list sang dictionary và xóa phần tử trùng nhau
listchieucaokhacnhautest = dict.fromkeys(hocsinh)
# Chuyển lại dictionary về list
listchieucaokhacnhau = list(listchieucaokhacnhautest)
chieucaotb2 = int(0)
for i in range(0,len(listchieucaokhacnhau)):
    chieucaotb2 = chieucaotb2 + int(listchieucaokhacnhau[i])
chieucaotb2 = chieucaotb2 / len(listchieucaokhacnhau)
print("Chieu cao khac nhau cua hoc sinh trong lop la: ", listchieucaokhacnhau)
print("Gia tri trung binh chieu cao khac nhau: ", chieucaotb2)