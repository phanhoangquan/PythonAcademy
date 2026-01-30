#Tính tuổi theo ngày
import math
songay=int(input())
nam=int(songay/365)
if nam>0:
 print(nam,"years")
thang=int((songay-(nam*365))/30)
if thang>0:
 print(thang, "months")
ngay=int(songay-((nam*365)+(thang*30)))
if ngay > 0:
 print(ngay, "days")
