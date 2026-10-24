"""
Question Q012: Age category

Problem statement:
Given age, print 'Child' if age < 13, 'Teen' if age is from 13 through 19, otherwise 'Adult'.

My approach (write this in your own words after thinking):
-

Test cases to try: 19,13,21
-
"""

# YOUR SOLUTION STARTS HERE

Age = int(input("Enter your age: "))
if(Age<13):
    print("Child")
elif(Age<=19):
    print("Teen")
else:
    print("Adult")