"""
Question Q001: Digit sum

Problem statement:
Given an integer n = 4725, print the sum of its digits without converting it to a string. Expected output: 18.

My approach (write this in your own words after thinking):
-

Test cases to try: 4725,45,8888
-
"""

# YOUR SOLUTION STARTS HERE

n = 4725
T = 0
while n>0:
    digit = n%10
    T = T + digit
    n = n//10
print("Sum =",T)

