# Target = num + compliment  ,  compliment = Target - num
def check_for_pair(lst,target):
    seen= set()
    for num in lst:
        compliment= target-num
        if compliment in seen:
            return True
        seen.add(num)
    return False
lst=list(map(int, input('enter the list: ').split()))
target=int(input('enter the target: '))
pair=check_for_pair(lst,target)
print('pair with given sum : ',pair)

'''
Example Walkthrough:
Let's take the list: [1, 2, 3, 4, 5] and the target sum: 9.

We want to find two distinct elements in the list that add up to 9.

Iteration Steps:
Initial Setup:
List: [1, 2, 3, 4, 5]
Target sum: 9
Seen set: set() (initially empty)
Iteration 1:
Current number: 1
Complement: 9 - 1 = 8
Check if 8 is in the seen set: No.
Add 1 to the seen set: seen = {1}.
Iteration 2:
Current number: 2
Complement: 9 - 2 = 7
Check if 7 is in the seen set: No.
Add 2 to the seen set: seen = {1, 2}.
Iteration 3:
Current number: 3
Complement: 9 - 3 = 6
Check if 6 is in the seen set: No.
Add 3 to the seen set: seen = {1, 2, 3}.
Iteration 4:
Current number: 4
Complement: 9 - 4 = 5
Check if 5 is in the seen set: No.
Add 4 to the seen set: seen = {1, 2, 3, 4}.
Iteration 5:
Current number: 5
Complement: 9 - 5 = 4
Check if 4 is in the seen set: Yes, it is.
This means we have found a pair that sums up to 9 (the pair is 4 and 5).
Return True because we've found the pair.
Final Output:
Since the pair 4 + 5 = 9 is found, the function returns True.
'''

