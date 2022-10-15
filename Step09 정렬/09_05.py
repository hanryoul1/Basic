import sys

lst = []
N = int(input())

for i in range(N):
    input_num = int(sys.stdin.readline())
    lst.append(input_num)

# 산술평균
a = round(sum(lst)/N)

# 중앙값
lst.sort()
b = lst[N//2]

# 최빈값


# 범위
c = lst[N-1] - lst[0]

print(a)
print(b)
print(c)



