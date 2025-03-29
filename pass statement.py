n=int(input("Enter the number:")) #input number
for x in range(n): #iterate for loop
    if x % 20 == 0: #condition 1
        print(x)
    elif x % 15 == 0: #condition 2
        pass #pass statement

    elif x % 5 == 0: #condition 3
        print(x) #display result
    elif x % 3 == 0: #condition 4
        print(x) #display result
    else: #condition 5
        print(x) #display result    