# 283.py
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
        
class bike(Car):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

bicycle = bike(2, 100)
print(bicycle.price)