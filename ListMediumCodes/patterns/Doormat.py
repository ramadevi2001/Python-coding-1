n,m = map(int,input('n is odd, and m is 3 times of n n*3: ').split())
for i in range(n//2):
    pattern='.|.'*(2*i+1)
    print(pattern.center(m,'-'))
print('WELCOME'.center(m,'-'))

for i in reversed(range(n//2)):
    pattern='.|.'*(2*i+1)
    print(pattern.center(m,'-'))
