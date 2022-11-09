N = int(input())
lst = list(map(int, input().split()))
V = int(input())
cnt = 0

for i in range(len(lst)):
    if lst[i] == V:
        cnt += 1

print(cnt)