nhap = input()
list2 = []
listend = []
list = nhap.split(" ")
## Liet ke cac tap con co hai phan tu
for i in range(0,len(list)):
    list2 = str(list[i])
    if len(list2)>1:
        listend.append(list2)
print("Cac tap con co hai phan tu la: ", listend)
print("So tap con co hai phan tu la: ", len(listend))
    
