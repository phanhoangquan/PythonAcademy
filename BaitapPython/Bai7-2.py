#giathua
def giai_thua(n):
    giatri = int(n)
    for i in range(1,n):
        giatri = giatri * (n-i)
    print(giatri)
print("Nhap vao so tu nhien n: ", end="")
n = int(input())
giai_thua(n)