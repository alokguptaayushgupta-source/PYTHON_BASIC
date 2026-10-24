"""
Question Q030: First and last digit

Problem statement:
Input a positive integer and print its first digit and last digit using arithmetic and loops.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
last = n%10
first = n
while(first>=10):
    first //= 10
print(f"First digit = {first}\nLast digit = {last}")
