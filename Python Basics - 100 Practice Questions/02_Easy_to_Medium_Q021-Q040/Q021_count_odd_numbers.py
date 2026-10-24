"""
Question Q021: Count odd numbers

Problem statement:
Input n and count the odd numbers from 1 through n.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
count = 0
for i in range (1,n+1):
    if(i%2!=0):
        count += 1
print(count)
