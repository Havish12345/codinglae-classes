def change(bill, paid):
    ta= paid - bill
    if ta > 0:
        print("paid amount is greater than bill amount",ta)
    
    
       




bill = float(input("enter the amount")) 
paid = float(input("enter the amount paid"))
change(bill, paid)  