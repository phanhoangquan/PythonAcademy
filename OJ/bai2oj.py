#Khoảng cách Euclid
import math
x1, y1, x2, y2=input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
kc = float(math.sqrt((x1-x2)**2+(y1-y2)**2))
print("%.4f" %kc)
