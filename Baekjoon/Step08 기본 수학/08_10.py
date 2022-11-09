# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2

import sys

M = int(sys.stdin.readline()) # 60
N = int(sys.stdin.readline()) # 100
result = []
# sum, small = 0, 0

for i in range(M, N+1): # 60 ~ 100
    for j in range(2, i+1):
        if i == j:
            result.append(i)

        if i % j == 0:
            break

if not result:
    print(-1)

else:
    print(sum(result))
    print(result[0])