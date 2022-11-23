# 201.py
def print_coin():
    print("비트코인")

# 202.py
print_coin()

# 203.py
for i in range(100):
    print_coin()

# 204.py
def print_coins():
    for i in range(100):
        print("비트코인")

# 205.py
"""
hello() 
def hello():
    print("Hi")

함수가 정의되기 전에 호출 -> 에러 발생
"""

# 206.py (A, B, C, A, B)
def message() :
    print("A")
    print("B")

message()
print("C")
message()


# 207.py (A, C, B)
print("A")

def message() :
    print("B")

print("C")
message()

# 208.py (A, C, B, E, D)
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

# 209.py (B, A)
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# 210.py (B, C, B, C, B, C, A)
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()