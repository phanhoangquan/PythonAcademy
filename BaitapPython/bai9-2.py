import math
list = []
chuoi = ""
for i in range(100,1000):
    list.append(i)
    chuoi = str(list[0])
    congsai = int(chuoi[1])-int(chuoi[0])
    congsai2 = int(chuoi[2])-int(chuoi[1])
    if congsai2 == congsai:
        print(i)
    list.remove(i)
