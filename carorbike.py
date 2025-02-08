print("hi can you tell me whan you prefer\n1)car\n2)bike")
veichle = input("Enter your choice: ")
if veichle == "car":
    print("what type of car do you prefer\n1)SUV\n2)Sedan")
    car = input("Enter your choice: ")
    if car == "SUV":
        print("wow thats a grate choice\nso for the SUV which company would you go for\n1)Tata\n2)Toyota \n3)mahindra")
        company = input("Enter your choice: ")
        if company == "Tata":
            print("Tata is a good company i would have gone for the safarrior the Hariar")
        elif company == "Toyota":
            print("Toyota is a good company i would have gone for the fortuner or the inova")
        elif company == "mahindra":
            print("mahindra is a good company i would have gone for the scorpio or the xuv500")
        else:
            print("please enter a valid choice")
    if car == "Sedan":
        print("wow thats a grate choice\nso for the Sedan which company would you go for\n1)Honda\n2)Hyundai \n3)Maruti")
        company = input("Enter your choice: ")
        if company == "Honda":
            print("Honda is a good company i would have gone for the city or the amaze")
        elif company == "Hyundai":
            print("Hyundai is a good company i would have gone for the verna or the i20")
        elif company == "Maruti":
            print("Maruti is a good company i would have gone for the swift or the baleno")
        else:
            print("please enter a valid choice")        
elif veichle == "bike":
    print("what type of bike do you prefer\n1)sport\n2)adventure")
    bike = input("Enter your choice: ")
    if bike == "sport":
        print("wow thats a grate choice\nso for the sport bike which company would you go for\n1)ninja\n2)KTM \n3)BMW")
        company = input("Enter your choice: ")
        if company == "ninja":
            print("ninja is a good company nice choice")
        elif company == "KTM":
            print("KTM is a good company nice choice")
        elif company == "BMW":
            print("BMW is a good company nice choice")
        else:
            print("please enter a valid choice")
    elif bike == "adventure":
        print("wow thats a grate choice\nso for the commuter bike which company would you go for\n1)royal enfind\n2)Honda\n3)yamha")
        company = input("Enter your choice: ")
        if company == "royal enfind":
            print("royal enfind is a good company ")
        elif company == "Honda":
            print("Honda is a good company ")
        elif company == "yamh":
            print("yamha is a good company ")
        else:
            print("please enter a valid choice1")
    else:
        print("please enter a valid choice2")
else :
    print("please enter a valid choice3")        
##
print("thank you for your time")