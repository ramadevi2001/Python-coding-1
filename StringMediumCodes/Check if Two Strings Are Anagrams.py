def Anagram(str1,str2):
    str1= str1.replace(" ","").lower()
    str2= str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
str1=input('enter  string1:')
str2=input('enter  string2:')
print(Anagram(str1,str2))
