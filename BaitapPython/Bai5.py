n=int(input())
kq=True
if n < 2:
    kq=False
elif n >=2:
    for i in range(2,n):
        if n%i==0:
            kq=False
if kq==True:
    print("So nay la so nguyen to")
elif kq==False:
    print("So nay khong phai la so nguyen to")