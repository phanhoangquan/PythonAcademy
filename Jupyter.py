def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print(uscln(3,6))