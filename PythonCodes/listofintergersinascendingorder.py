try:
  lst=list(map(int,input('enter list:').split()))
  lst.sort()
  print(lst)
except ValueError:
  print('enter valid integers')