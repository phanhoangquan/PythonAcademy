print("Nhap chieu rong: ")
m=int(input())
print("Nhap chieu dai: ")
n=int(input())
if n>m and n>0 and m>0:
  for i in range(1,m+1):
     if i==1 or i==m:
        for j in range(1,n+1):
          print("*", end="")
        print()
     else:
        for j in range(1,n+1):
            if j==1 or j==n:
                print("*", end="")
            else:
                print(" ", end="")
        print()