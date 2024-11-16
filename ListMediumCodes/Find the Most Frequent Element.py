# From the collection modult importing the Couter class to use its functionalities and find the  most frequent element in list
from collections import Counter
def most_frequent_element(lst):
    count=Counter(lst)
    most_common_element=count.most_common(2) # here the most_common() is used for finding most common element, and the number in it is used to find the how many elements we want to see the frequency 
    return most_common_element[0][0]
lst=list(map(int,input('enter the list').split()))
print(most_frequent_element(lst))

'''
most_common_element=count.most_common(2) = it returns the tuple with (frequent element, count) 
return most_common_element[0][0] = it takes the first tuple from the list and  item from the tuple 

'''