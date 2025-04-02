print('Hi enter your age')
try:
    age = (input('Enter your age: '))
    if age%2==0:
        print('even number')
    else:
        print('odd number')
     
except ValueError as e:
    print("Invalid input: ")

except NameError as e:
    print("Name error: ")
except TypeError as e:
    print("Type error: ") 
finally:
    print("Thank you for using the age checker.") 
  



