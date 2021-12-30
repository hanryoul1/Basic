h, m = map(int, input().split()) 

if h == 0:
    if m >= 45:
        m = m - 45
    elif m < 45:
        h = 23
        m = m + 15

elif h > 0:
    if m >= 45:
        m = m - 45
    elif m < 45:
        h = h - 1
        m = m + 15

print(str(h), str(m))