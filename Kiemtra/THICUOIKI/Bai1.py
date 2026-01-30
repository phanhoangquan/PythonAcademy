import re
print("Nhap chuoi:",end="")
n = input()
lst = re.findall('[a-zA-z]', n)
for i in lst:
    print(i,end='')
