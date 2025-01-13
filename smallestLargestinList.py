def findSmallLarge(numbers):
    smallest=numbers[0]
    largest=numbers[0]
    for num in numbers:
        if num<smallest:
            smallest=num
        if num>largest:
            largest=num
    return smallest,largest
numbers=list(map(int,input('enter the list:').split()))
smallest,largest=findSmallLarge(numbers)
print('the smallest no:',smallest)
print('the largest no:',largest)