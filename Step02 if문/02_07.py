a, b, c = map(int, input().split())
award = 0

if (a == b) and (b == c):
    award = 10000 + a * 1000

elif (a == b):
    award = 1000 + a * 100

elif (b == c):
    award = 1000 + b * 100

elif (a == c):
    award = 1000 + c * 100
    
else:
    award = max(a, b, c) * 100

print(award)