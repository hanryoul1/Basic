import sys
N = int(sys.stdin.readline())
nums = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    nums.append([x, y])

nums = sorted(nums)

for i in range(N):
    print(nums[i][0], nums[i][1])