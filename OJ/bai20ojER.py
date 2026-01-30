def sochinnut(n):
    sum = int(0)
    for i in range(1,n+1):
        chuoi = str(i)
        if 1<=i<=9:
          if i%10==9:
            sum+=1
        elif 10<=i<=99:
          if (int(chuoi[0])+int(chuoi[1]))%10==9:
            sum+=1
        elif 100<=i<=999:
          if (int(chuoi[0])+int(chuoi[1])+int(chuoi[2]))%10==9:
            sum+=1
        elif 1000<=i<=9999:
          if (int(chuoi[0])+int(chuoi[1])+int(chuoi[2])+int(chuoi[3]))%10==9:
            sum+=1
        elif 10000<=i<=99999:
          if (int(chuoi[0])+int(chuoi[1])+int(chuoi[2])+int(chuoi[3])+int(chuoi[4]))%10==9:
            sum+=1
        elif 100000<=i<=999999:
          if (int(chuoi[0])+int(chuoi[1])+int(chuoi[2])+int(chuoi[3])+int(chuoi[4])+int(chuoi[5]))%10==9:
            sum+=1
    print(sum)
##############MAIN################
n=int(input())    
if 1<=n<=10**6:
    sochinnut(n)