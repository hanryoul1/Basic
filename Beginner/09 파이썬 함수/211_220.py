# 211.py (안녕, Hi)
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

# 212.py (7, 15)
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

# 213.py
def 함수(문자열) :
    print(문자열)
    # 함수를 호출할 때 하나의 파라미터를 입력해야함

# 214.py
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
#문자열과 숫자는 더할 수 없다는 에러 발생

# 215.py
def print_with_smile(word):
    print(word + ":D")

# 216.py
print_with_smile("안녕하세요")

# 217.py
def print_upper_price(price):
    print(price * 1.3)

# 218.py
def print_sum(a, b):
    print(a+b)

# 219.py
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

# 220.py
def print_max(a, b, c):
    if a > b and a > c:
        print(a)

    elif b > a and b > c:
        print(b)

    else:
        print(c)

print_max(7, 4, 20)

"""
def print_max(a, b, c):
    max_val = 0
    if a > max_val :
        max_val = a
    
    if b > max_val:
        max_val = b
    
    if c > max_val:
        max_val = c
"""