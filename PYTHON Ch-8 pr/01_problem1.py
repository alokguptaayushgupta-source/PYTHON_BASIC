def num(num1,num2,num3):
    if(num1==num2==num3):
        return "All are equal"
    elif(num1>=num2 and num1>=num3):
        return "num1 is greatest"
    elif(num3>=num1 and num3>=num2):
        return "num3 is greatest"
    else:
        return "num2 is greatest"

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print(num(num1,num2,num3))
