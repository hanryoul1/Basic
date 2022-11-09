#  킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# EX) [2 1 2 1 2 1] => [-1 0 0 1 0 7]

chess = list(map(int, input().split()))
num = []

for i in range(0, 2):
    num.append(1 - chess[i])

for j in range(2, 5):
    num.append(2 - chess[j])

num.append(8 - chess[5])

for k in range(0, 6):
    print(num[k], end = " ")