

units=int(input("Enter the number of units: "))
if units<50:
    amount=units*2.60
    surcharge=25
elif units<=100:
    amount=units*2.60
    surcharge=25
elif units<=200:
    amount=units*3.25
    surcharge=25
else:
    amount=units*4.00
    surcharge=25
total=amount+surcharge
print(total)

