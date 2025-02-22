print("enter the number to find the total digits in it")
num = int(input())
sum = 0
while num > 0:
    sum += 1
    num = num // 10
print("Total digits in the number is: ", sum)


