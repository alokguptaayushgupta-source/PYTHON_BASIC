A = int(input("Enter your age: "))

if(A%2==0):
    print("A is evan")
if(A>=18):
    print("you are above the age of consent")

elif(A<0):
    print("you are intering invalid negativ age")

elif(A==0):
    print("you are intering 0 which is invalid age")

else:
    print("you are below the age of consent")


print("End of the program")