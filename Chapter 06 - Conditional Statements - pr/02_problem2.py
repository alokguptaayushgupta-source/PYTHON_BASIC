marks1 = int(input("Enter tour marks: "))
marks2 = int(input("Enter tour marks: "))
marks3 = int(input("Enter tour marks: "))

totalmarks = (100*(marks1+marks2+marks3)/300)

if(totalmarks>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Hurry You are pass",totalmarks,"%")

else:
    print("Sorry you are fail, try again next year")
