# 277.py
import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999) # 0 이상, 999 이하
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 계좌번호는 3자리-2자리-6자리 형태
        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(5) # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3 
        Account.account_count += 1

    @ classmethod
    def get_account_num(self):
        return self.account_count
    
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
        
        if self.deposit_count % 5 == 0:
            self.balance += self.balance * 0.01

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        
    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)

q = Account("자바", 10000)
q.deposit(10000)
q.deposit(10000)
q.deposit(10000)
q.deposit(10000)
q.deposit(10000)
print(q.balance)