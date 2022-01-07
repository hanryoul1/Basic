cnt = int(input())  # 과목 수
num_list = list(map(int, input().split()))
m = max(num_list)

mid_list = []
for i in num_list:
    mid_list.append(i/m*100)

result = sum(mid_list)/cnt
print(result)
    