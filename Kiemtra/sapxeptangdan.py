n = [3,4,2,6]
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            tm = n[i]
            n[i] = n[j]
            n[j] = tm
print(n)
