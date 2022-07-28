class Bank:
    def __init__(self):
        self.Balance = 0
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.Balance+= amount
        print(f"amount deposited is {amount}")
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.Balance > amount:
            self.Balance -= amount
            print(f"amount withrawn is {amount}")
        else:
            print(f"Insufficient balance")
            
    def Total(self):
        print(f"net available balance is {self.Balance}")
        

account = Bank()
account.deposit()
account.withdraw()
account.Total()