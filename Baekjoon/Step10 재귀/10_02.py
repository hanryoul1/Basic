N = int(input())

def cal(N):
    if N == 0 or N == 1:
        return N
    return cal(N-2) + cal(N-1)

print(cal(N))
    