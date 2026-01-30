x, y=map(int, input().split())
if x>0 and y>0 or x>0 and y=0:
    print("The coordinate point (%d,%d) lies in the I quandrant" %(x,y))
elif x<0 and y>0 or x=0 and y>0:
    print("The coordinate point (%d,%d) lies in the II quandrant" %(x,y))
elif x<=0 and y<0 or x<0 and y<=0:
    print("The coordinate point (%d,%d) lies in the III quandrant" %(x,y))
elif x>=0 and y<0 or x>0 and y<=0:
    print("The coordinate point (%d,%d) lies in the IV quandrant" %(x,y))
else:
    print("The coordinate point (%d,%d) lies at theorigin" %(x,y))
