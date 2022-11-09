num_list = []
result_list = []

for i in range(10):
    num_list.append(int(input()))

for j in range(10):
    result_list.append(num_list[j]%42)

result_list = set(result_list) # set으로 변경하여 중복요소 제거
result_list = list(result_list) # 다시 list로 변경
print(len(result_list)) # 요소 개수 출력