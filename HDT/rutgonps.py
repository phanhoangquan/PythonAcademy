def rutgonps(a,b):
    if a>b :
      for i in range(2, b+1):
       if a%i == 0 & b % i == 0:
         return [int(a/i),int(b/i)]
    else:
      for i in range(2, a+1):
       if a%i == 0 & b % i == 0:
         return [int(a/i),int(b/i)]
x=int(3)
y=int(4)
print(rutgonps(x,y))