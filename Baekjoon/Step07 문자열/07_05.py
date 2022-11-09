s = input().upper()  # s = MISSISSIPI / str 내부 모든 알파벳을 대문자로 변경
s_list = list(set(s))  # s_list = ['M', 'I', 'S', 'P']
result = []

for i in s_list:
    count = s.count(i)  # i = M, I, S, P
    result.append(count)  # result = [1, 4, 4, 1]

if result.count(max(result)) >= 2:
    print("?")
else:
    print(s_list[(result.index(max(result)))])