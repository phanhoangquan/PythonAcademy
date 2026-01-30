list = []
list2 = []
n = int(input())
##
for i in range(0,n):
    pt = int(input())
    list.append(pt)
## 
for i in range(0,n):
    if list[i]>10 and list[i]%2==0:
        list2.append(list[i])
print(list2)
        