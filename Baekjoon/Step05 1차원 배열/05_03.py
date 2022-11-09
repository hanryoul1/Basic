a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))
    # count를 사용하여 그 리스트에 문자가 몇 개씩 있는지 print