# Palindrome(팰린드롬) : 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# EX) AAA, ABBA, ABABA 
# def isPalindrome() : 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0 return

def recursion(S, l, r):
    global cnt
    cnt += 1
    if (l >= r):
        return 1
    elif (S[l] != S[r]):
        return 0
    else:
        return recursion(S, l+1, r-1)

def isPalindrome(S):
    return recursion(S, 0, len(S)-1)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        cnt = 0
        S = input()
        print(isPalindrome(S), cnt)