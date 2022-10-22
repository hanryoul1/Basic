# Palindrome(팰린드롬) : 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# EX) AAA, ABBA, ABABA 
# def isPalindrome() : 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0 return

import sys
input = sys.stdin.readline

T = int(input())
result = 0
cnt = 0

for i in range(T):
    S = input()

    def isPalindrome(S):
        for i in range(0, S(len)):
            if S[i] == S[S(len)-1-i]:
                result = 1
            else:
                result = 0
        return result