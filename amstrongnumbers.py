number=int(input("Enter a 3 digit number: "))
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if number==sum:
    print("it is a amstrong number")
else:
    print("it is not a amstrong number")    

