import math
n = int(input())
so = int(0)
i = int(1)
while(n>0):
  sodu = n%2
  so = so+(sodu*i)
  n = int(n / 2)
  i = i*10
print(so)