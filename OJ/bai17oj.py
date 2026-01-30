n = int(input())
a,b= map(int, input().split())
sum = int(0)
if 1<=n<=(10**4) and 1<=a<=b<=36:
 for i in range(1,n+1):
    chuoi = str(i)
    if 1<=i<=9:
        if a<=i<=b:
            sum+=i
    elif 10<=i<=99:
        if a<=(int(chuoi[0])+int(chuoi[1]))<=b:
            sum+=i
    elif 100<=i<=999:
        if a<=(int(chuoi[0])+int(chuoi[1])+int(chuoi[2]))<=b:
            sum+=i
    elif 1000<=i<=9999:
        if a<=(int(chuoi[0])+int(chuoi[1])+int(chuoi[2])+int(chuoi[3]))<=b:
            sum+=i
    elif i==10000:
        if a<=1000<=b:
            sum+=i
print(sum)