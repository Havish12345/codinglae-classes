def bill(bill_amt, tip_percent ):
    total_amt = bill_amt*( 1+0.01*tip_percent)  
    print("The total amount is ", total_amt) 
    
bill_amt = int(input("enter the amount"))
tip_percent = int(input("enter the tip percentage"))

bill(bill_amt, tip_percent)
bill(1000, 10)

    