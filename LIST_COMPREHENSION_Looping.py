mylist_square=[i**2 for i in range(1,6)]
print(mylist_square)
for i in mylist_square:
    print(i)
lis1=[1,3,5,7]
lis2=[2,4,6,8]
pair=[(x,y) for x in lis1 for y in lis2 if x!=y]
print(pair)