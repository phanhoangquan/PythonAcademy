#Biện luận phương trình bậc nhất a*x+b=0
import math
x=float()
print("Nhap vao so a: ")
a=float(input())
print("Nhap vao so b: ")
b=float(input())
if a != 0:
    x=-b/a
    print("Phuong trinh co nghiem duy nhat x=%f" %x)
if a == 0:
    if b == 0:
        print("Phuong trinh co nghiem voi moi x thuoc R")
    elif b!= 0:
        print("Phuong trinh vo nghiem")
    
