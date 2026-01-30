#Capsonhan
def cap_so_nhan(n):
    sohangdau = int(7)
    for i in range(n):
        sohangdau = sohangdau + 2
    print("Vay thu hang %d co gia tri la: " %(n),sohangdau)
print("Nhap so thu hang: ",end="")
n = int(input())
cap_so_nhan(n)