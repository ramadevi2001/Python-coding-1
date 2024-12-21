def prime(n):
    for i in range(2,n):
        if n%i ==0:
            return 'not prime'
    else:
        return 'prime'
n = int(input('enter n:'))
print(prime(n))

# list of prime numbers upto N

def prime_up_toN(n):
    prime =[]
    for i in range(2,n+1):
        is_prime =True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    return prime
n = int(input('enter n:'))
print(prime_up_toN(n))
