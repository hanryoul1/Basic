cnt = int(input())
result = cnt

for i in range(cnt):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:
            result -= 1
            break

print(result)