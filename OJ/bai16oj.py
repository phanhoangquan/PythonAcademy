##Nhap so phan tu , nhap phan tu cach nhau dau cach
n = int(input())
list = [int(n) for n in input().split()]
##
kc = int(0)
for i in range(n):
    sodu = list[i]%19
    if sodu == 0 or sodu == 3 or sodu == 6 or sodu == 9 or sodu == 11 or sodu == 14 or sodu == 17:
        kc = kc + 1
print(kc)