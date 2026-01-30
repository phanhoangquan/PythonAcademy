n=int(input())
s= n%2
if s==1:
    print("Số lẻ")
elif s==0 and n>=100:
    print("Số chẵn và lớn hơn hoặc bằng 100")
else:
    print("Số chẵn và bé hơn 100")
        
