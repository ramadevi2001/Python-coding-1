def palindrome(lst):
    if lst==lst[::-1]:
        print( 'palindrome')
    else:
        print('not a palindrome')

lst=list(map(int,input('enter the list:').split()))
palindrome(lst)