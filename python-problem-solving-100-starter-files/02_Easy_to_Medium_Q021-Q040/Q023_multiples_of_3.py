"""
Question Q023: Multiples of 3

Problem statement:
Input n and print all numbers from 1 through n that are divisible by 3.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

N = int(input("Enter a number: "))
for i in range(1,N+1):
    if(i%3==0):
        print(i)
        