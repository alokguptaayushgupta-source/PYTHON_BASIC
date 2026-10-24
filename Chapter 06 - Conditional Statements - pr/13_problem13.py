a = int(input("Enter your first number: "))
b = int(input("Enter your secand number: "))
c = a%10
d = b%10

if(c == d):
    print("same last digit")
else:
    print("last digit not same")