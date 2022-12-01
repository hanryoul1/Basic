# 271.py
import random

class Account:
    def __init__(self, name, balance):
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

Han = Account("한률", 10000000000000000000000000000000000)
print(Han.name)
print(Han.balance)
print(Han.bank)
print(Han.account_number)
