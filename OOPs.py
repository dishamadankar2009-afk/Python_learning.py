class Account:
    def __init__(self, bal, account):
        self.balance = bal
        self.account_no = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance is =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(7000, 123456)

acc1.debit(1000)
acc1.credit(1500)
