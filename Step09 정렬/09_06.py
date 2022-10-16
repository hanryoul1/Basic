import sys
lst = []
N = sys.stdin.readline()

for i in range(len(N)):
    lst.append(N[i])

lst.sort(reverse = True)
print("".join(lst))