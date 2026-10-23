"""
Question Q029: Reverse digits

Problem statement:
Input a positive integer and print its digits in reverse order as a number. Example: 472 gives 274.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a positive number: "))
rev = 0 
while n > 0:
    dig = n%10
    rev = rev *10 + dig
    n = n // 10
print(rev)
