x = "Phan Hoang Quan"
email = ""
n =int(0)
for i in range(len(x)):
    if n==2:
     if x[i]==" ":
        email = email+x[i+1:len(x)]
        break
    if n==1:
     if x[i]==" ":
        email = email+x[i+1]
        n=2
    if n==0:
     email = email+x[0]
     n=1
print(email.lower()+"@email.com")
