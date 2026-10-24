"""
Question Q020: Sum of even numbers

Problem statement:
Input n and calculate the sum of all even numbers from 1 through n using a loop.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    if(i%2==0):
        sum += i
print(sum)