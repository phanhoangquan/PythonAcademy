List = []
n = int(input())
## Thêm giá trị vào list
for i in range(0,n):
    pt = int(input())
    List.append(pt)
## Tìm phần tử lớn nhất
print(max(List))