#Hệ phương trình bậc nhất 2 ẩn
import math
x=int(input())
if 1<=x<=10:
 for i in range(x):
    a1,b1,c1,a2,b2,c2=map(float, input().split())
    D=float((a1*b2)-(a2*b1))
    Dx=float((c1*b2)-(c2*b1))
    Dy=float((a1*c2)-(a2*c1))
    if D==Dx==Dy==0:
        print("Many solutions")
    elif D!=0:
        x1=float(Dx/D)
        x2=float(Dy/D)
        print("%.6f %.6f" %(x1,x2))
    else:
        print("No solution")