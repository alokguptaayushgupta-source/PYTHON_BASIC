"""
Question Q037: Keep a running sum

Problem statement:
Input 5 numbers one by one. Print the total sum after all 5 inputs.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    total += number
print("Total sum =",total)
