# fibanocci sequence upto given limit n
def fibanocci(n):
    fib_seq=[0,1]
    while fib_seq[-2]+fib_seq[-1]<n:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
    return fib_seq
n= int(input('enter n:'))
print(fibanocci(n))

# fib seq upto n

def fibonocciupton(n):
    fib_seq=[0,1]
    while len(fib_seq)<n:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
    return fib_seq
n=int(input('enter n:'))
print(fibonocciupton(n))