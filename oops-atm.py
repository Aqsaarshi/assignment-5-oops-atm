class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234      

    def check_pin(self,input_pin):
        """Verify if the entered pin matches the store pin"""
        if input_pin == self.pin:
            print("Correct Pin")
            return True
        else:
            print("Incorrect Pin")
            return False

    def check_balance(self):
        """Display the current account balance"""
        print(f"Your current balance is :{self.balance} rupees.")

    def deposit(self,amount):   
        """Add money to the account (requires valid PIN)"""

        if amount <=0:
            print("Deposit amount must be positive")

        else:
            self.balance += amount
            print(f"Deposit {amount} rupees successfully!!!!")

    def withdraw (self,amount:int):
        """Remove money from the account (requires valid PIN and sufficient balance)"""
        if amount <=0:
            print("with draw amount must be positive")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print(f"Withdraw {amount} rupees successfully!!!")


    def exit(self):
        """Terminate the program"""

        print("Thank you for using the ATM . Goodbye!!")
        exit()            

atm = ATM()
if atm.check_pin(int(input("🔐 Enter PIN: "))):
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. WithDraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = int(input("Enter Amount To Deposit:"))
            atm.deposit(amount)
        elif choice == '3':
            amount = int(input("Enter Amount To Withdraw:"))
            atm.withdraw(amount)
        elif choice == '4':
            atm.exit()
        else:
            print("Invalid choice .PLEASE TRY AGAIN.")        


