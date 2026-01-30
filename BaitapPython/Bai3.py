#Biện luận phương trình bậc hai a*x**2+b*x+c=0
import math
x=float()
denta=float()
print("Nhap vao so a: ")
a=float(input())
print("Nhap vao so b: ")
b=float(input())
print("Nhap vao so c: ")
c=float(input())
if a==0:
    if b!=0:
        x=-c/b
        print("Phuong trinh co nghiem duy nhat x=%.2f" %x)
    if b==0:
        if c==0:
            print("Phuong trinh co ngiem voi moi x thuoc R")
        elif c!=0:
            print("Phuong trinh vo nghiem")
if a!=0:
    denta=(b**2)-(4*a*c)
    if denta<0:
        print("Phuong trinh vo nghiem")
    elif denta==0:
        x=-b/(2*a)
        print("Phuong trinh co nghiem kep x=%.2f" %x)
    else:
        sqrtdenta=math.sqrt(denta)
        x1=(-b-sqrtdenta)/(2*a)
        x2=(-b+sqrtdenta)/(2*a)
        print("Phuong trinh co hai nghiem x1=%.2f /d x2=%.2f" %(x1,x2))
        
        
        
    
    