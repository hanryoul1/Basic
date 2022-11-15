환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}

user = input("입력: ")
money, currency = user.split()

result = float(money) * 환율[currency]
print(result, "원")