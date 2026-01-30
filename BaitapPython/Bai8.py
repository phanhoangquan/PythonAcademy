print("Nhap chieu rong: ")
m=int(input())
print("Nhap chieu dai: ")
n=int(input())
if n>m and n>0 and m>0:
  for i in range(m):
     print("*"*n)
else:
    print("Day khong phai la hinh chu nhat")