#Công thức Heron
import math
a,b,c= map(float, input().split())
if a>=b+c or b>=a+c or c>=a+b:
    print("No Solution")
else:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("%.6f" %s)