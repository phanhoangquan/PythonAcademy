#Người dùng nhập vào một năm là một số nguyên dương bất kỳ. Cho biết năm đó có là năm nhuận hay không

print("Nhập vào một năm bất kỳ:")
x=int(input())
if x>0:
    if x%100==0:
        if x%400==0:
            print("Năm %d là năm nhuận" %x)
        else:
            print("Năm %d không phải là năm nhuận" %x)
    elif x%4==0:
        print("Năm %d là năm nhuận" %x)
    else:
        print("Năm %d không phải là năm nhuận" %x)

 