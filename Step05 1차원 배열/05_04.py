num_list = []
result_list = []

for i in range(10):
    num_list.append(int(input()))

for j in range(10):
    result_list.append(num_list[j]%42)

result_list = set(result_list)
result_list = list(result_list)
print(len(result_list))