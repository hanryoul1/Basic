# # Solution_MY1
# import sys
# M, N = map(int, sys.stdin.readline().split())

# for i in range(M, N+1): # 3~16
#     error = 0
#     for j in range(2, i): # i = 3
#         if i % j == 0:
#             error += 1
#     if error == 0:
#         print(i)

# # Solution_MY2
# import sys
# M, N = map(int, sys.stdin.readline().split())
# nums = list(map(int, range(M, N+1))) # 3~16

# for num in nums:
#     error = 0
#     for i in range(2, num): # 2부터 n-1까지
#         if num % i == 0:
#             error += 1
#     if error == 0:
#         print(num)

# Solution
M, N = map(int, input().split())

def prime(k):
    if k == 1:
        return 0
    
    for i in range(2, int(k ** 0.5)+1): # range(n, k)는 시간초과
        if k % i == 0:
            return 0
    
    return 1

for i in range(M, N+1):
    if prime(i):
        print(i)