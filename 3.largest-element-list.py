list1= list(map(int,input('enter the list:').split()))
large_elemnt=list1[0]
for i in list1:
    if i>large_elemnt:
        large_elemnt=i
print(large_elemnt)

print(max(list1))# built-in function