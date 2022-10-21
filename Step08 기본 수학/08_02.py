N = int(input())
t, line = 1, 1

while N > t:
    t += 6 * line
    line += 1

print(line)