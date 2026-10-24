"""
Question Q028: Count digits

Problem statement:
Input a positive integer and count its digits using a loop. Example: 8042 gives 4.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
count = 0
if(n==0):
    count = 1
else:
    while (n>0):
        count += 1
        n//=10
print(count)
