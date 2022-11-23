# 221.py
def print_reverse(word):
    print(word[::-1])
print_reverse("python")

# 222.py
def print_score(lst):
    sum = 0
    for score in lst:
        sum += score
    print(sum / len(lst))
print_score([1, 2, 3])

"""
def print_score(lst):
    print(sum(lst)/len(lst))
"""

# 223.py
def print_even(lst2):
    for num in lst2:
        if num % 2 == 0:
            print(num)
print_even([1, 3, 2, 10, 12, 11, 15])

# 224.py
def print_keys(dic):
    for key in dic.keys():
        print(key)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225.py
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict, date):
    print(dict[date])

print_value_by_key(my_dict, "10/26")

# 226.py
def print_5xn(line):
    chunk_num = int(len(line) / 5)

    if len(line) % 5 == 0:
        for x in range(chunk_num) :
            print(line[x * 5: x * 5 + 5])
    
    else:
        for x in range(chunk_num + 1) :
            print(line[x * 5: x * 5 + 5])

print_5xn("아이엠어보이유알어걸스")

# 227.py
def print_mxn(string, n):
    chunk_num = len(string) // n

    if len(string) % 3 == 0:
        for y in range(chunk_num):
            print(string[y * n: y * n + n])

    else:
        for y in range(chunk_num + 1):
            print(string[y * n: y * n + n])
            
print_mxn("아이엠어보이유알어걸", 3)

# 228.py
def calc_monthly_salary(salary):
    print(salary // 12)

calc_monthly_salary(13000000)

# 229.py (왼쪽: 100 / 오른쪽:200)
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 230.py (왼쪽: 200 / 오른쪽:100)
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)