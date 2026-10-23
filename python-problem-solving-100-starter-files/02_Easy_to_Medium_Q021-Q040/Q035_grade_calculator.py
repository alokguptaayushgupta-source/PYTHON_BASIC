"""
Question Q035: Grade calculator

Problem statement:
Input marks from 0 to 100. Print A for 90+, B for 75–89, C for 60–74, D for 40–59, otherwise F.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

mark = int(input("Enter your marks: "))
if(mark>=90):
    print("A")
elif(mark>=75):
    print("B")
elif(mark>=60):
    print("C")
elif(mark>=40):
    print("D")
else:
    print("F")
