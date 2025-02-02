
weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in cm: "))

BMI=weight/(height/100)**2
print("your BMI is ",BMI)
if BMI<18:
    print("you are underweight")
elif BMI>18 and BMI<23:
    print("you are normal")
elif BMI>23 :
    print("you are healthy")