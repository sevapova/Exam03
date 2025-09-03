'''6. Encapsulation
Task: BankAccount classida balans private bo‘lsin.'''

class BankAccount:
    def __init__(self, balans):
        self.__balans = balans   

    def deposit(self, amount):
        if amount > 0:
            self.__balans += amount
            print(f"{amount} so'm qo'shildi.")
        else:
            print("Xato!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balans:
            self.__balans -= amount
            print(f"{amount} so'm yechildi.")
        else:
            print("Yetarli mablag' yo'q!")

    def get_balance(self):
        return self.__balans


acc = BankAccount(100)
print("Balans:", acc.get_balance())  
acc.deposit(50)                     
acc.withdraw(30)                    
print("Balans:", acc.get_balance())  
