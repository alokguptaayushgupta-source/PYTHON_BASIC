"""
Question Q038: Count positives

Problem statement:
Input 8 numbers and count how many are positive, negative, and zero.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

positive = 0
negative = 0
zero = 0
for i in range(8):
    num = int(input("Enter a number: "))
    if(num>0):
        positive += 1
    elif(num<0):
        negative += 1
    else:
        zero += 1

print("Positive =",positive)
print("Negative =",negative)
print("Zero =",zero)
