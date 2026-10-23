"""
Question Q032: Leap year check

Problem statement:
Input a year and determine whether it is a leap year using the standard divisibility rules.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

Y = int(input("Enter a year: "))
if(Y>999 and Y<10000):
    if(Y%4==0 and Y%100!=0 or Y%400==0):
        print(Y,"Is a leap year")
    else:
        print(Y,"Is not a leap year")
else:
    print(Y,"Enter valid year")
    