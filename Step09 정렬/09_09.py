lst = []
new_lst = []
N = int(input())

for i in range(N):
    word = input()
    lst.append(word)

lst.sort()
lst.sort(key = len)

for j in lst:
    if j not in new_lst:
        print(j)
        new_lst.append(j)