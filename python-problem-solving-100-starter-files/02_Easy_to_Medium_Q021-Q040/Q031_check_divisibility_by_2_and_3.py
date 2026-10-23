"""
Question Q031: Check divisibility by 2 and 3

Problem statement:
Input n and print whether it is divisible by both 2 and 3.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
if(n%2==0 and n%3==0):
    print("Number is divided by both 2 and 3: ",n)
else:
    print("Not divided by both 2 and 3: ",n)
