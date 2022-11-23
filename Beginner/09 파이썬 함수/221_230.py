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
# def print_5xn(string):

# 227.py
# 228.py
# 229.py
# 230.py