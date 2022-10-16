import sys
N = int(sys.stdin.readline())
nums = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    nums.append([y, x])

nums.sort()

for i in range(N):
    print(nums[i][1], nums[i][0])