"""
Question Q039: Average and pass status

Problem statement:
Input marks for 5 subjects. Print the average and 'Pass' only if every subject mark is at least 33; otherwise print 'Fail'.

My approach (write this in your own words after thinking):
-

Test cases to try:
-
"""

# YOUR SOLUTION STARTS HERE

totalmarks = 0
allsubject = True
for i in range(5):
    marks = int(input("Enter a number: "))
    totalmarks += marks
    if(marks < 33):
        allsubject = False
    average = totalmarks//5
if(allsubject):
    print(average,"Pass")
else:
    print("Fail")
