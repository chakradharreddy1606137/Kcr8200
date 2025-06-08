balance=0
while True:
    
    def menu_dis():
        print("\n Atm menu: ")
        print("1.credit :")
        print("2. Debit:")
        print("3.Balance Enquiry:")
        print("4. Exit :")
     
        choice=input("enter your choice from (1-4):")

        if choice=="1":
            credit()
    
        elif choice=="2":  
            debited() 
        elif choice=="3":
             Balance()
        elif choice=="4":
            Exit()
            
        else:
            print("choice from (1-4 )only")
        
    def credit():
        global balance
    
        amount=float(input("enter amount to be credited:"))
        if amount<=0:
            print("enter positive values only ")
        else:
            balance+=amount
            print(f"  {amount} the amount is credited")
        
    def debited():
        global balance
        amount=float(input("enter debited amount:"))
        if amount<=0:
            print("the amount must be positive only")
        elif amount >balance:
            print("  Insufficent funds")
        else:
            balance-=amount
            print(f"   {amount} is debited successfully ")   
         
    def Balance():
        global balance
        print(f"  {balance} it is the remaining balance " )
    
    def Exit():
        print("Thank you for using atm ,Goodbye!")
        exit()
        

    menu_dis()
         
    

    
    
    

    
    
    
    
    
    
         
    
        
    