try:
   lst=list(map(int, input('enter the list:').split()))
   if len(lst)<2:
      print('it will contain atleast two numbes')
   else:
      unique_Elements=list(set(lst))
      unique_Elements.sort()
      if len(unique_Elements)<2:
         print('not possible to find 2nd largest')
      else:
         print(f'the second largest elemetn in a list is {unique_Elements[-2]}')
except ValueError:
   print('enter valid intergers')
   


