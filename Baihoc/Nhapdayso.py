##Nhập số phần tử của dãy số
n = int(input("Nhập số phần tử của dãy số : "))
mylist = []
for i in range(n):
   val = int(input('Nhập một số: '))
   mylist.append(val)
print(mylist)
##Nhập số phần tử của dãy số
n = int(input("Nhập số phần tử của dãy số : "))
s = [int(input(">>")) for i in range(n)]
print(s)
##Nhập các phần tử của dãy số cách nhau bởi dấu cách
mystr = input("Nhập các phần tử của dãy số cách nhau bởi dấu cách: ")
mylist = mystr.split()
mylistnum = [int(i) for i in mylist]
print(mylistnum)
## Nhập dãy số trong python không giới hạn số phần tử
mylistnum = []
print('Nhập "stop" khi muốn dừng')
while True:
    val = input('Nhập một số: ')
    if val == 'stop':
        print('Kết thúc')
        break
    mylistnum.append(int(val))
print(mylistnum)