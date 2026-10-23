"""
Question Q034: Middle value

Problem statement:
Input three distinct numbers and print the middle value (neither largest nor smallest), without sorting.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your secand number: "))
n3 = int(input("Enter your third number: "))
if(n1<n2 and n1>n3 or n1>n2 and n1<n3):
    print(n1)
elif(n2<n1 and n2>n3 or n2>n1 and n2<n3):
    print(n2)
else:
    print(n3)



'''
this is secand mathed to solve this
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your secand number: "))
n3 = int(input("Enter your third number: "))
if(n1>n2>n3 or n1<n2<n3):
    print(n2)
elif(n2>n1>n3 or n2<n1<n3):
    print(n1)
else:
    print(n3)
'''