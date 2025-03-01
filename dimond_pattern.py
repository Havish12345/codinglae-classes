row=(int(input("Enter the number of rows: ")))
if row%2==0:
    halfdimond=int(row/2)
else:
    halfdimond=int(row/2)+1
space=halfdimond-1
for i in range(1,halfdimond+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(1,2*i):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range (1,halfdimond):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfdimond-i)):
        print(end=str(num))
        num=num+1
    print()
    






































































