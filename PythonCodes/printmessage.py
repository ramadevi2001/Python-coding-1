name = input('enter the name:')
print(f'Hello {name}')

# print um

a= int(input('enter a:'))
b= int(input('enter b:'))
c=a+b
print(f'the sum is {c}')

# odd even

n= int(input('enter n:'))
if n% 2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

# largest of 3 numbers

a= int(input('enter a:'))
b= int(input('enter b:'))
c= int(input('enter c:'))
if a >b and a>c:
    print(a,'is the largest')
elif b>a and b>c:
    print(b, 'is the largest')
else:
    print(c, 'is the largest')

# pinting 1 to 10 numbers

for i in range(1,11):
    print(i)

# multiplication table of a n

n= int(input('enter the n:'))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
# sum of all numbers from 1 to 100

a=1
sum=0
while a <= 100:
    sum+=a
    a +=1
print(' sum of all numbers from 1 to 100 is:',sum)


    

