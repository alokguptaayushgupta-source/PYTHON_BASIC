"""
Question Q018: Multiplication table

Problem statement:
Input n and print its multiplication table from n x 1 through n x 10.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
t = 0
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")