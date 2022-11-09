s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in s:
        print(s.index(i), end =' ')
    else:
        print(-1, end = ' ')  # 한칸씩 띄어서 반환하기 때문에 출력이후 한칸을 띄우는 end=' ' 사용