c1 = 'Make a lot of money'
c2 = "buy now"
c3 = "subscrib this"
c4 = "click this"

messege = str(input("Enter your comment: "))

if(c1 in messege or c2 in messege or c3 in messege or c4 in messege):
    print("this comment is spam")

else:
    print("this comment is not spam")