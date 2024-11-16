def move_zeros(lst):
    nonZeroIndex=0
    for i in range(len(lst)):
        if lst[i]!=0:
            lst[nonZeroIndex]=lst[i]
            nonZeroIndex+=1
    for i in range(nonZeroIndex,len(lst)):
        lst[i]=0
    return lst
lst=list(map(int,input('enter the list:').split()))
result=move_zeros(lst)
print('zeros moved to end:',result)

'''
Input List: [0, 1, 0, 3, 12]
non_zero_index: 0 (we start here to place the first non-zero number)
First Loop (Moving Non-Zero Elements to the Front)
In this first part, we are only concerned with finding non-zero numbers and moving them to the beginning of the list.

Iteration 1 (i = 0)

Current Element: 0
Since it’s 0, we skip it and do nothing.
non_zero_index: 0 (still waiting to place the first non-zero number)
Iteration 2 (i = 1)

Current Element: 1
It’s a non-zero number.
We place 1 at the position of non_zero_index, which is 0.
The list now looks like: [1, 1, 0, 3, 12]
Update: Increase non_zero_index to 1 (the next spot for a non-zero number)
Iteration 3 (i = 2)

Current Element: 0
It’s zero, so we skip it.
non_zero_index: 1 (no change)
Iteration 4 (i = 3)

Current Element: 3
It’s a non-zero number.
We place 3 at non_zero_index, which is 1.
The list now looks like: [1, 3, 0, 3, 12]
Update: Increase non_zero_index to 2
Iteration 5 (i = 4)

Current Element: 12
It’s a non-zero number.
We place 12 at non_zero_index, which is 2.
The list now looks like: [1, 3, 12, 3, 12]
Update: Increase non_zero_index to 3
After the first loop, our list is partially done: [1, 3, 12, 3, 12].

We’ve moved all the non-zero numbers to the front.
non_zero_index is now 3, meaning everything from position 0 to 2 is non-zero.
Second Loop (Filling Remaining Elements with Zeros)
Now we use non_zero_index to know where to start filling in zeros. We’ll replace everything from position 3 onward with zeros.

Iteration 1 (i = 3)

We set lst[3] to 0.
The list now looks like: [1, 3, 12, 0, 12]
Iteration 2 (i = 4)

We set lst[4] to 0.
The list now looks like: [1, 3, 12, 0, 0]
'''