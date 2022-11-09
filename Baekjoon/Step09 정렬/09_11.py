import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
s = sorted(set(l)) # set -> 중복제거
d = {s[i]:i for i in range(len(s))} # dic 사용

for i in l:
    print(d[i], end = " ")


# l = 2, 4, -10, 4, -9
# s = -10, -9, 2, 4
#      0    1  2  3

# d = {-10:0, -9:1, 2:2, 4:3}

# d[2], d[4], d[-10], d[4], d[-9]
#  2      3      0      3      1