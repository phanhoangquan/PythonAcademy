import math
print("Nhap vao so hoc sinh: ", end="")
hocsinh = int(input())
print("Nhap vao so ban hoc Tieng Anh: ", end="")
tienganh = int(input())
print("Nhap vao so ban hoc Tieng Phap: ", end="")
tiengphap = int(input())
print("So ban hoc ca hai thu tieng do: ", end="")
twothutieng = int(input())
sobanhoctienganh = tienganh - twothutieng
sobanhoctiengphap = tiengphap - twothutieng
sobankhonghoc = hocsinh - ( sobanhoctienganh + sobanhoctiengphap + twothutieng )
print("Vay so ban khong hoc ca 2 thu tieng la: ", sobankhonghoc) 
