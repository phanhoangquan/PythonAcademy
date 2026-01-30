#Tích hai số
import math
a,b = input().split()
a=int(a)
b=int(b)
s=int(a*b)
if s%2 == 0:
    print("Even")
else:
    print("Odd")