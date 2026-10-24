"""
Question Q010: Larger of two

Problem statement:
Given two numbers a and b, print the larger number. If they are equal, print 'Equal'.

My approach (write this in your own words after thinking):
-

Test cases to try: 5:99,45:44,55:55
-
"""

# YOUR SOLUTION STARTS HERE

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
if (a>b):
    print("The larger number =",a)
elif (b>a):
    print("The larger number =",b)
else:
    print("Equal")
