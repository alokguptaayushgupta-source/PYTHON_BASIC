"""
Question Q040: Print numbers in a range

Problem statement:
Input start and end. Print every integer from start to end, including both endpoints. Assume start <= end.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
for i in range(n1,n2+1):
    print(i,end=" ")
    