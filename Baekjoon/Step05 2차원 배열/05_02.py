# Solution_MY
lst = []
new_lst = []
num = 0

for i in range(9):
    lst.append(list(map(int, input().split())))
    for j in range(9):
        if lst[i][j] >= num:
            num = lst[j][j]
            new_lst.append([i, j])

print(num)
print(new_lst[0][0], end=" ")
print(new_lst[0][1])

# Solution
max_num = 0

for i in range(9):
    row = list(map(int, input().split())) # 행렬 저장 필요X

    if max(row) >= max_num:
        max_num = max(row)
        x = i + 1 # 행
        y = row.index(max_num) + 1 # 열

print(max_num)
print(x, y)