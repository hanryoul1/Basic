# 181.py
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]

# 182.py
stock = [[100, 80], [200, 210], [300, 330]]

# 183.py
stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}

# 184.py
stock = {"10/10":[80, 110, 70, 90], "10/11":[210, 230, 190, 200]}

# 185.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호")

# 186.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for p in apart[::-1]:
    for q in p:
        print(q, "호")

# 187.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for m in apart[::-1]:
    for n in m[::-1]:
        print(n, "호")

# 188.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호")
        print("-" * 5) # ("-----")

# 189.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for p in apart:
    for q in p:
        print(q, "호")
    print("-" * 5)

# 190.py
apart = [ [101, 102], [201, 202], [301, 302] ]
for m in apart:
    for n in m:
        print(n, "호")
print("-" * 5)