class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner                          # public
        self._account_type = "Checking"             # protected
        self.__account_number = account_number      # private
        self.__balance = balance                    # private


    @property
    def account_number(self):
        return self.__account_number
# read-only — no setter defined

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = amount
            
acc = BankAccount("Ana", "ACC-1001", 500)
print(acc.owner, acc.account_number, acc.balance)
acc.balance = 700
