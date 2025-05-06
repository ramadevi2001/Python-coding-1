def rotatearraybyKsteps(lst,k):
    k%=len(lst )
    return lst[-k:]+lst[:-k]
lst=list(map(int,input('enter lst:').split()))
k=int(input('enter K:'))
print(rotatearraybyKsteps(lst,k))


def fact(n):
    facttorial=1
    for i in range(1, n+1):
        facttorial*=i
        return facttorial
n= int(input('enter n:'))
print(fact(n))