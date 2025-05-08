def fibonocciseriesupton(n):
    fib_seq=[0,1]

    while fib_seq[-2]+fib_seq[-1]<n:
#while len(fib_seq)<n: ' then we get the length upto the n numbers'
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
    return fib_seq
n=9
print(fibonocciseriesupton(n))




    
        