import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.round = 100

    def deposit(self, amount, round):
        for i in range(round):
            balance = self.balance
            time.sleep(0.05)
            self.balance = balance + amount
            print("deposit ", i, " round, for: +", amount)

    def withdraw(self, amount, round):
        for i in range(round):
            balance = self.balance
            time.sleep(0.07)
            self.balance = balance - amount
            print("withdraw ", i, " round, for: -", amount)

b = BankAccount()
t1 = threading.Thread(target=b.deposit, args=(100,b.round,))
t2 = threading.Thread(target=b.withdraw, args=(50,b.round,))

t1.start()
t2.start()

t1.join()
t2.join()

print("final balance should be ", 50*b.round, ", but: ", b.balance)
