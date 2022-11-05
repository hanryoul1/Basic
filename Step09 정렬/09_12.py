# Solution_MY
import sys
lst = []
sum = 0

for i in range(5):
    a = int(sys.stdin.readline())
    lst.append(a)
    sum += a

lst.sort()
print(sum//5)
print(lst[2])

# Solution
nums = [int(input()) for i in range(5)]
nums.sort()

print(sum(nums)//5)
print(nums[2])