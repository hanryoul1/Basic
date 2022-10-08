n = int(input())
cnt = 0

if (n % 5) % 3 == 0:
    cnt += (n / 5)
    n = (n % 5)
    cnt += (n / 3)

elif (n % 3) == 0:
    cnt += (n / 3)

else:
    cnt = -1

print(cnt)