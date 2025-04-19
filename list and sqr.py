print("this program will see is the first and last digit of a number are the same and if so it will the sqr  and arrange all odd answers at one side and even answers on another side")

def counter(num):
    list = []
    for i in num:
        if len(i)>1 and i[0]==i[-1]:
            list.append(i)       
    print("The elements in the list are: ", list)
    list1 = [int(i)**2 for i in list]
    print("The square of the elements in the list are: ", list1)
    list2 = [i for i in list1 if i%2==0]
    list3 = [i for i in list1 if i%2!=0]
    print("The even elements in the list are: ", list2)
    print("The odd elements in the list are: ", list3)
    return list, list1, list2, list3


num = counter(["101", "12321", "12345", "67876", "54345","543","678", "123456789", "987654321", "11111"])
