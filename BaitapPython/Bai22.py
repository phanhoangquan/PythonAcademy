def chuoi(str1, str2):
    if len(str1)>len(str2):
        print(str1)
    elif len(str1)<len(str2):
        print(str2)
    else:
        print(str1, end="\n")
        print(str2)
chuoi(str1=input(), str2=input())