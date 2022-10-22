T = int(input()) #테스트 케이스

for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    zero_User = list(range(1, n+1))
    
    for x in range(k):
        for y in range(1, n):
            zero_User[y] += zero_User[y-1] #리스트 안에서 1층 인원수로 교체
    
    print(zero_User[-1]) #리스트의 제일 마지막 출력