cart = [10,20,30,500,60,40]
for item in cart:
    if item >= 500:
        print("we cannot process the cart")
        break
    print(item)
else:
    print("congrat your item process succesfully")