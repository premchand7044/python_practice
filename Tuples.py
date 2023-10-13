a=(1,2,3,4,5)
b=(6,7,8,9,0)
del a
del b
a=()
print(a)
a=(1,)
print(a)
a=1,2,3,4
print(a)
a=(10,20,30,40)
b=(50,60,70,80)
print(len(a))
c=a+b
print(c)
print(a*2)
print(10 in a)
print(100 in a)
print(10 not in a)
print(100 not in a)
for ele in a:
    print(ele)
d= max(a)
print(d)
print(min(a))
print(a.index(10))
f=(a*2)
print(f.count(10))
str="premchand"
print(tuple(str))
my_List=[10,20,30,40,50]
print(tuple(my_List))