n=int(input("enter the number you want to convert into binary:"))
while n>0:
    remainder=n%2
    n=n//2
    print(remainder,end="")


