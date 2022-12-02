# 285.py
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Car_moto(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def info(self):
        print(f"바퀴수 {self.wheel}")
        print(f"가격 {self.price}")

class bike(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        # 차.__init__(self, wheel, price)
        # self.wheel = wheel
        # self.price = price
        self.system = system

car = Car_moto(4, 1000)
car.info()