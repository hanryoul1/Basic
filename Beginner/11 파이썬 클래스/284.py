# 284.py
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
        
class bike(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        # 차.__init__(self, wheel, price)
        # self.wheel = wheel
        # self.price = price
        self.system = system

bicycle = bike(2, 100, "시마노")
print(bicycle.system)
print(bicycle.wheel)