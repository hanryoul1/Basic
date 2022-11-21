# 171.py
price_list = [32100, 32150, 32000, 32500]
for price in price_list:
    print(price)

# 172.py
for i in range(len(price_list)):
    print(i, price_list[i])

for i, data in enumerate(price_list):
    print(i, data)
    # enumerate() 함수
    # 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)
    # 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)

# 173.py
for j, data in enumerate(price_list):
    print(len(price_list) - 1 - j, data)

for j in range(len(price_list)):
    print(len(price_list) - 1 - j, price_list[j])

# 174.py
for k in range(1, 4):
    print(90 + 10*k, price_list[k])

# 175.py
my_list = ["가", "나", "다", "라"]
for l in range(len(my_list) - 1):
    print(my_list[l], my_list[l+1])

for l in range(1, len(my_list)):
    print(my_list[1 - l], my_list[l])

# 176.py
my_list2 = ["가", "나", "다", "라", "마"]
for h in range(len(my_list2) - 2): # (0, 3)
    print(my_list2[h], my_list2[h+1], my_list2[h+2])

for h in range(1, len(my_list2) - 1): # (1, 4)
    print(my_list2[h - 1], my_list2[h], my_list2[h+1])

for h in range(2, len(my_list2)): # (2, 5)
    print(my_list2[h - 2], my_list2[h - 1], my_list2[h])

# 177.py
my_list3 = ["가", "나", "다", "라"]
for m in range(len(my_list3), 1, -1): # (4 - 3 - 2)
    print(my_list3[m - 1], my_list3[m - 2])

for m in range(len(my_list3) - 1, 0, -1): # (3 - 2 - 1)
    print(my_list3[m], my_list3[m - 1])

# 178.py
my_list4 = [100, 200, 400, 800] 
for n in range(len(my_list4) - 1): # (0, 3)
    print(my_list4[n+1] - my_list4[n])

# 179.py
my_list5 = [100, 200, 400, 800, 1000, 1300] 
for p in range(len(my_list5) - 2):
    print((my_list5[p] + my_list5[p + 1] + my_list5[p + 2]) / 3)
    # 0, 1, 2
    # 1, 2, 3
    # 2, 3, 4
    # 3, 4, 5

# 180.py
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for q in range(len(low_prices)):
    gap = high_prices[q] - low_prices[q]
    volatility.append(gap)

print(volatility)