a = int(input("Enter your order amount: "))
d = 30
if(a<500):
    print(f"{a+d} rupees to pay {d} rupees is delivery charge")
else:
    print(f"Free delivery {a} rupees to pay ")