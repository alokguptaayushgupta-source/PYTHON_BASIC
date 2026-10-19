"""
Question Q017: Sum from 1 to n

Problem statement:
Input n and use a loop to calculate 1 + 2 + ... + n.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum =",sum)