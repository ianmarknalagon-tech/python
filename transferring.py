class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def tranfer_to(self, other, amount):
        self.balance -= amount
        other.balance += amount
        print(self.owner, "sent", amount, "to", other.owner)

acc1 = BankAccount ("Ana", 500)
acc2 = BankAccount ("Ben", 100)
print(acc1.owner, acc1.balance)
print(acc2.owner, acc2.balance)
acc1.tranfer_to(acc2, 150)
print(acc1.owner, acc1.balance)
print(acc2.owner, acc2.balance)
acc1.tranfer_to(acc2, 250)
print(acc1.owner, acc1.balance)
print(acc2.owner, acc2.balance)