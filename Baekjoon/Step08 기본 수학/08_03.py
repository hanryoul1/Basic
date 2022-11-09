X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    print(f"{X}/{line+1-X}")

else:
    print(f"{line+1-X}/{X}")