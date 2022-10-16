import sys
from collections import Counter

N = int(input())
input_num = [int(sys.stdin.readline()) for i in range(N)]

"""
for i in range(N):
    input_num = int(sys.stdin.readline())
    lst.append(input_num)
"""

# 산술평균
a = round(sum(input_num)/N)

# 중앙값
input_num.sort()
b = input_num[N//2]

# 최빈값
cnt = Counter(input_num).most_common(2) # 가장 개수가 많은 k개의 데이터를 리턴

if len(cnt) > 1: # 데이터가 2개 이상일 경우
    if cnt[0][1] == cnt[1][1]:
        d = cnt[1][0]

    else:
        d = cnt[0][0]

else:
    d = cnt[0][0]

# 범위
c = input_num[N-1] - input_num[0]

print(a)
print(b)
print(d)
print(c)