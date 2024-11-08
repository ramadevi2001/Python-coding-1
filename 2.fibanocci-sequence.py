# fibanocci sequence upto given limit n
def fibanocci(n):
    fib_seq=[0,1]
    while fib_seq[-2]+fib_seq[-1]<n:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
    return fib_seq
n= int(input('enter n:'))
print(fibanocci(n))

# fib seq upto n

def feb(n):
    feb_seq=[0,1]
    while len(feb_seq)<n:
        feb_seq.append(feb_seq[-2]+feb_seq[-1])
        
    return feb_seq
n=int(input('enter n:'))
print(feb(n))