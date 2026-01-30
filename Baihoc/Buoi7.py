from bisect import bisect_right

##

warn = ['red','yellow','orange']
sortedwarn = warn.sort()
print(warn)
print(warn.sort())
print(sortedwarn)

cool = ['grey','green','blue']
sortedcool = sorted(cool)
print(cool)
print(sorted(cool))
print(sortedcool)

##

warn = ['yellow', 'orange']
hot = ['red']
brightcolors = [warn]
brightcolors.append(hot)
print(brightcolors)
hot.append('pink')
print(hot)
print(brightcolors)


## xoa phan tu


def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    print(L1)
L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1, L2)

##tra cuu tu tien


grades = {'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
print(grades['John'])
grades['Sylvan'] = 'A'
print('John' in grades)
print('Daniel' in grades)
del(grades['Ana'])
print(grades)
print(grades.keys())
print(grades.values())

