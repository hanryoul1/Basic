N, M = map(int, input().split())
A, B = [], []

for i in [A, B]:
    for j in range(N):
        i.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

    print(*A[i])
    # print(A[i]) 
    # [4, 4, 4]
    # [6, 6, 6]
    # [5, 6, 100]