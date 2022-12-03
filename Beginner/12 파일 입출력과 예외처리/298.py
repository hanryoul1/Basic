# 298.py
# 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생
# ZeroDivisionError 에러만 예외처리

try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")