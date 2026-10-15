a1 = float(input("Enter your number: "))
a2 = float(input("Enter your number: "))
a3 = float(input("Enter your number: "))
a4 = float(input("Enter your number: "))

if(a1>a2 and a1>=a3 and a1>=a4):
    print("gretest number is a1:",a1)

elif(a2>a1 and a2>=a3 and a2>=a4):
    print("gretest number is a2:",a2)

elif(a3>a2 and a3>a1 and a3>=a4):
    print("gretest number is a3:",a3)


else:
    print("All number are equl")