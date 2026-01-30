s = str(input())
hoa = 0
thuong = 0
for c in s:
    if c.isupper():
            hoa += 1
    if c.islower():
            thuong += 1
print("So tu viet hoa:", hoa)
print("So tu viet thuong:", thuong)
