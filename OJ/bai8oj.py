#Giải phương trình bậc hai
import math
a,b,c= map(float, input().split())
if a!=0:
    denta = b**2-(4*a*c)
    if denta < 0:
        print("No solution")
    elif denta == 0:
        x = -b/(2*a)
        print("%.4f" %x)
    else:
        sqrtdenta = math.sqrt(denta)
        x1 = (-b-sqrtdenta)/(2*a)
        x2 = (-b+sqrtdenta)/(2*a)
        print("%.4f" %x2)
        print("%.4f" %x1)
        