def xu_ly_chuoi(s):
    so = ""
    chu = ""
    for i in s:
        ck = ord(i)
        if ck > 47 and ck <58:
            so += i
        elif (ck > 64 and ck <91) or (ck > 96 and ck <123):
            chu += i
    print("Số chữ số là:",len(so))
    print("Số chữ cái là:",len(chu))
s = input("nhap chuoi:") 
xu_ly_chuoi(s)