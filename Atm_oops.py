class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def credited(self):
        amount = int(input("Enter your credit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"The amount is credited successfully: {amount}")
        else:
            print("The amount must be positive.")

    def debited(self):
        amount = int(input("Enter your debit amount: "))
        if amount <= 0:
            print(f"Please enter a valid  positive amount: {amount}")
        elif amount> self.balance:
            print("its insufficient funds !!")
            
        else:  
           self.balance -= amount
           print(f"The amount is debited successfully: {amount}")

    def balanced(self):
        print(f"Total balance: {self.balance}")


class Atm(Bank):
    def exits(self):
        print("Exiting... Thank you!")
        exit()

    def menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Credit")
            print("2. Debit")
            print("3. Balance Enquiry")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.credited()
            elif choice == "2":
                self.debited()
            elif choice == "3":
                self.balanced()
            elif choice == "4":
                self.exits()
            else:
                print("Invalid choice. Please select between (1-4).")


# Run the ATM system
sai = Atm()
sai.menu()
