import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

cnt = (V-B) / (A-B) # (5-1) / (2-1)
    
if cnt != int(cnt): # (6-1) / (5-1)
    cnt += 1

print(int(cnt))