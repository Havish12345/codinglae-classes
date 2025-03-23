
try:
    input1=int(input("Enter the number:"))
    input2=int(input("Enter the number:"))
    result=input1/input2
    print(result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:   
    print("Please enter only numbers")
except:
    print("An error occured")
finally:
    print("Execution completed")
