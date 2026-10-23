"""
Question Q025: Factorial

Problem statement:
Input n (n >= 0) and calculate n! using a loop. For example, 5! = 120.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter a number: "))
Factorial = 1
for i in range(1,n+1):
    Factorial *= i
print(Factorial)
