#Phân biệt tam giác
a,b,c= map(float, input().split())
if a==b==c:
    print("Tam giac deu")
elif a==b or b==c or c==a:
    print("Tam giac can")
else:
    print("Tam giac thuong")