n = int(input())
chuoi = str(n)
dem = int(0)
if -(10**18)<=n<=10**18:
 for i in range(len(chuoi)):
   if (int(chuoi[i]))%2!=0:
        dem = dem + 1
print(dem)