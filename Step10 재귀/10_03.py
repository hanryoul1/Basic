# Palindrome(팰린드롬) : 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# EX) AAA, ABBA, ABABA 
# def isPalindrome : 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0 return
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    S = input()