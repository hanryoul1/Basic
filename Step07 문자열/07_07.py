a, b = map(int, input().split())

a = str(a)
b = str(b)

a = a[2] + a[1] + a[0]
b = b[2] + b[1] + b[0]

if int(a) > int(b):
    print(a)

else:
    print(b)