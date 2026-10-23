"""
Question Q036: Number guessing feedback

Problem statement:
Set a secret number in the code. Input a guess and print 'Too low', 'Too high', or 'Correct'.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

Input = int(input("Enter a number: "))
Secret = 27
if(Input>Secret):
    print("Too high")
elif(Input<Secret):
    print("Too low")
else:
    print("Correct")
    