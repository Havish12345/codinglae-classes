upper=int(input("Enter the upper limit: "))
lower=int(input("enter the lower limit"))
for i in range(upper,lower+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    