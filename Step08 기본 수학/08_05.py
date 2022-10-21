# Solution_MY
import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    Y = N % H
    X = (W // Y) - 1
    
    if N % H == 0:
        Y = H
        X = N // H

    print(f"{Y}0{X}")

# Solution
import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    Y = N % H
    X = N // H + 1
    
    if N % H == 0:
        Y = H
        X = N // H
        
    print("%d%02d"%(Y, X)) # -> print(f"{Y}0{X}")