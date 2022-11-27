# 231.py
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)
# # 함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능
# # (local 변수) -> return 사용

# 232.py
def make_ulr(string):
    url = "www." + string + ".com"
    return url

make_ulr("naver")
print(make_ulr("naver"))

# 233.py
def make_list(words):
    lst = []
    for i in range(len(words)):
        lst.append(words[i])
    return lst

make_list("abcd")
print(make_list("abcd"))

# 234.py
def pickup_even(nums):
    num_list = []
    for num in nums:
        if num % 2 == 0:
            num_list.append(num)
    return num_list

pickup_even([3, 4, 5, 6, 7, 8])
print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235.py
def convert_int(n):
    return int(n.replace(',', ''))
        
convert_int("1,234,567")
print(convert_int("1,234,567"))

# 236.py
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c) # 22

# 237.py
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c) # 22

# 238.py
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c) # 140

# 239.py
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c) # 16

# 240.py
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c) # 28