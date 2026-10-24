"""
Question Q014: Simple discount

Problem statement:
Given price and discount percentage, calculate the final price after discount.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

p = int(input("Enter your price: "))
d = int(input("Enter your discoun %: "))
print(f"Final price after discount = {p-(d/100)*p}₹")