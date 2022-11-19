me = input("주민등록번호: ")
num1 = me.split("-")[0] # ['821010']
num2 = me.split("-")[1] # ['1635210']
lst1 = list(range(2, 8)) # 2, 3, 4, 5, 6, 7
lst2 = [8, 9, 2, 3, 4, 5]
result = 0

for i in range(len(num1)): 
    result += int(num1[i]) * lst1[i]

for j in range(len(num2)-1):
    result += int(num2[j]) * lst2[j]

result = 11 - (result % 11)

if str(result)[-1] == num2[6]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")