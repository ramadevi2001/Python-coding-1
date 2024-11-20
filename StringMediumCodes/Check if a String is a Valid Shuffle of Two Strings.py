def shuffle_or_not(str1,str2,shuffle):
    if len(shuffle) != len(str1)+len(str2):
        return False
    i, j =0,0 
    for char in shuffle:
        if i<len(str1) and char==str1[i]:
            i +=1
        elif j < len(str2) and char==str2[j]:
            j +=1
        else:
            return False
    return i == len(str1) and j==len(str2)
str1=input('enter the str:')
str2=input('enter the str:')
shuffle=input('enter the str:')
print("Is valid shufle:",shuffle_or_not(str1,str2,shuffle))


        