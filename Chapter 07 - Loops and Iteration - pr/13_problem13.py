n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n,i,-1):
        print("j",end=" ")
    print()