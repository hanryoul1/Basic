t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    s = str(s)

    for j in range(len(s)):
        print(s[j]*r, end='')  # 줄 바꿈과 공백 없이 뒤에 쓰게 만들기
    print()