l = [1,4,7,9]
for item in l:
    print(item)

else:
    print("Done")




cart = [10,20,30,50,60,40]
for item in cart:
    if item >= 500:
        print("we cannot process the item")
        break
    print(item)
else:
    print("congrat your item process succe")