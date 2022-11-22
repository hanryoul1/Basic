# 191.py
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for i in data:
    for j in i:
        print(j * 1.00014) # (j * 100.014 / 100)

# 192.py
for i in data:
    for j in i:
        print(j * 1.00014)
    print("----")

# 193.py
result = []
for m in data:
    for n in m:
        print(n * 1.00014)
        result.append(n * 1.00014)
print(result)

# 194.py
result = []
for m in data:
    sub = []
    for n in m:
        sub.append(n * 1.00014)
    result.append(sub)
print(result)

# 195.py
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for p in ohlc[1:]:
    print(p[3])

# 196.py
for p in ohlc[1:]:
    if p[3] > 150:
        print(p[3])

# 197.py
for p in ohlc[1:]:
    open = p[0]
    close = p[3]
    if close >= open:
        print(p[3])

# 198.py
volatility = []
for p in ohlc[1:]:
    change = p[1] - p[2]
    volatility.append(change)

print(volatility)
    
# 199.py
for p in ohlc[1:]:
    open = p[0]
    close = p[3]
    if close > open:
        print(p[1] - p[2])

# 200.py
money = 0
for p in ohlc[1:]:
    money += (p[3] - p[0])
print(money)