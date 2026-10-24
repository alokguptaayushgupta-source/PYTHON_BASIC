"""
Question Q013: Pass or fail

Problem statement:
Given marks out of 100, print 'Pass' if marks are at least 40; otherwise print 'Fail'.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

marks = int(input("Enter your marks: "))

if(marks <= 100):
    if(marks>=40):
        print("Pass")
    else:
        print("Fail")
else:
    print("Your mars is not valid try again")