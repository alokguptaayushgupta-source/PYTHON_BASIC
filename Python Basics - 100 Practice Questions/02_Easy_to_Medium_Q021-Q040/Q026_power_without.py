"""
Question Q026: Power without **

Problem statement:
Input base and a non-negative exponent. Calculate base raised to that exponent using a loop, without using **.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

Base = int(input("Enter a number: "))
Expo = int(input("Enter a number: "))
calc = 1
for i in range(1,Expo+1):
    calc *= Base
print(calc)
