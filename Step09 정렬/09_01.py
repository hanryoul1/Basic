lst = []

n = int(input())

for j in range(n):
    num = int(input())
    lst.append(num)

lst.sort()

for i in range(n):
    print(lst[i])