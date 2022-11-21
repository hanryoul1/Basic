# 151.py
lst1 = [3, -20, -3, 44]
for i in lst1:
    if i < 0:
        print(i)
    # else:
    #     pass

# 152.py
lst2 = [3, 100, 23, 44]
for j in lst2:
    if j % 3 == 0:
        print(j)

# 153.py
lst3 = [13, 21, 12, 14, 30, 18]
for h in lst3:
    if (h < 20) and (h % 3 == 0):
        print(h)

# 154.py
lst4 = ["I", "study", "python", "language", "!"]
for k in lst4:
    if len(k) >= 3:
        print(k)

# 155.py
lst5 = ["A", "b", "c", "D"]
for l in lst5:
    if l.isupper():
        print(l)

# 156.py
for m in lst5:
    if m.islower():
        print(m)

# 157.py
lst7 = ['dog', 'cat', 'parrot']
for n in lst7:
    print(n[0].upper() + n[1:]) # 변경한 대문자와 나머지 문자를 이어붙이기

# 158.py
lst8 = ['hello.py', 'ex01.py', 'intro.hwp']
for o in lst8:
    word = o.split(".")[0]
    print(word)

# 159.py
lst9 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for p in lst9:
    split = p.split(".")[1]
    
    if split == "h":
        print(p)

# 160.py
for q in lst9:
    split = q.split(".")[1]

    if split == "h" or split == "c":
        print(q)
