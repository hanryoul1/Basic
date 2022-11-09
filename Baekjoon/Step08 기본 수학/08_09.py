# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1

import sys

N = int(sys.stdin.readline()) # 4 
nums = list(map(int, input().split())) # 1 3 5 7
cnt = 0

for num in nums:
    error = 0
    if num > 1:
        for i in range(2, num): # 2부터 n-1까지
            if num % i == 0:
                error += 1
        
        if error == 0:
            cnt += 1

print(cnt)