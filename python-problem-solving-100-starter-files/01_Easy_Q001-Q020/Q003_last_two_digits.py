"""
Question Q003: Last two digits

Problem statement:
Given n = 153, print its last two digits. Expected output: 53.

My approach (write this in your own words after thinking):
-

Test cases to try: 153,568,555
-
"""

# YOUR SOLUTION STARTS HERE

n = int(input("Enter Test case: "))
print(f"Last two digit = {n%100}")