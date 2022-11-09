import sys
N = int(input())
lst = []

for i in range(N):
    [x, y] = sys.stdin.readline().split()
    lst.append([int(x), y])

lst.sort(key = lambda a: (a[0]))

# lambda function
# def temp(a):
#   return (a[0])

for a in lst:
    print(a[0], a[1])