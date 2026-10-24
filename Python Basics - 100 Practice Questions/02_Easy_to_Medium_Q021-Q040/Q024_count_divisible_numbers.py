"""
Question Q024: Count divisible numbers

Problem statement:
Input n and count numbers from 1 through n that are divisible by both 3 and 5.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        count += 1
print(count)
