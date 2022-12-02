# 286.py
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print(f"바퀴수 {self.wheel}")
        print(f"가격 {self.price}")

class bike(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system

bicycle = bike(2, 100, "시마노")
bicycle.info() # 부모 클래스 Car의 info()