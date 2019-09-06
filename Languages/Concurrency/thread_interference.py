import threading

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        balance = self.balance
        self.balance = balance + amount
    
    def withdraw(self, amount):
        balance = self.balance
        self.balance = balance - amount
    
b = BankAccount()
t1 = threading.Thread(target=b.deposit, args=(100,))
t2 = threading.Thread(target=b.withdraw, args=(50,))

t1.start()
t2.start()
