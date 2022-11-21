# 161.py
for i in range(100):
    print(i)

# 162.py
for j in range(2002, 2051, 4):
    print(j)

# 163.py
for k in range(1, 31):
    if k % 3 == 0:
        print(k)

# 164.py
for l in range(100):
    print(99 - l)

for l in range(99, -1, -1):
    print(l)

# 165.py
for h in range(10):
    print("0." + str(h))
    print(h / 10)

# 166.py
for m in range(1, 10):
    print("3x" + str(m) + " =", 3*m)

# 167.py
for n in range(1, 10, 2):
    print("3x" + str(n) + " =", 3*n)

# 168.py
result = 0
for o in range(1, 11):
    result += o
print("합:", result)

# 169.py
result2 = 0
for p in range(1, 11, 2):
    result2 += p
print("합:", result2)

# 170.py
result3 = 1
for q in range(1, 11):
    result3 *= q
print("곱:", result3)