def pattern(n):
    result = ''
    for i in range(1,n+1):
        for j in range(i,n+1):
          result+='*' 
        result+='\n'
    return result
n = int(input('enter n:'))
print(pattern(n))

# from 1 * to n * 
def pattern(n):
   result=''
   for i in range(1,n+1):
      result+= '*' * i
      result +='\n'
   return result
n=int(input('enter n:'))
print(pattern(n))   