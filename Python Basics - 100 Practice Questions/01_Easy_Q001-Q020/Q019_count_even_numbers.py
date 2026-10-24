"""
Question Q019: Count even numbers

Problem statement:
Input n. Use a loop to count how many even numbers exist from 1 through n.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n= int(input("Enter a number: "))
T = 0
for i in range(1,n+1):
    if(i%2==0):
        T += 1
print(T)