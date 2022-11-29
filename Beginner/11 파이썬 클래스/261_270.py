# 261.py
class Stock:
    pass

# 262.py
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

samsung = Stock("삼성전자", "005930")
print(samsung.name)
print(samsung.code)

# 263.py
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자") # Stock.set_name(a, "삼성전자")
print(a.name)
print(a.code)

# 264.py
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.name)
print(a.code)

# 265.py
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code

    # def get_name(self):
    #     print(self.name)
    
    # def get_code(self):
    #     print(self.code)

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

samsung = Stock("삼성전자", "005930")
# samsung.get_name()
# samsung.get_code()
print(samsung.get_name())
print(samsung.get_code())

# 266.py
class Stock:
    def __init__(self, name, code, per, pbr, rev):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.rev = rev

# 267.py
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(samsung.name)
print(samsung.code)
print(samsung.per)
print(samsung.pbr)
print(samsung.rev)

# 268.py
class Stock:
    def __init__(self, name, code, per, pbr, rev):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.rev = rev

    def set_per(self, per):
        self.per = per
    
    def set_pbr(self, pbr):
        self.pbr = pbr
    
    def set_rev(self, rev):
        self.rev = rev

# 269.py
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
samsung.set_per(12.75) # Stock.set_per(samsung, 12.75)
print(samsung.name)
print(samsung.code)
print(samsung.per)
print(samsung.pbr)
print(samsung.rev)

# 270.py
class Stock:
    def __init__(self, name, code, per, pbr, rev):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.rev = rev

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

lst = [samsung, hyundai, lg]
for company in lst:
    print(company.code, company.per) 
    # company -> Stock class 객체를 바인딩하기 때문