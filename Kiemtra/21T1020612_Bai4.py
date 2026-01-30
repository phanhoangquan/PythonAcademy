print("Nhap n: ")
n = int(input())
mystr = input("Nhập các phần tử của dãy số cách nhau bởi dấu cách: ")
mylist = mystr.split()
mylistnum = [int(i) for i in mylist]
for i in range(len(mylistnum)):
  x =int(0)
  if (i+1)<len(mylistnum):
    if int(mylistnum[i])>int(mylistnum[i+1]):
        print("No")
        x = int(1)
        break
if x == 0:
    print("Yes")
    

        