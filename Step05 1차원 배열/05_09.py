student = list(range(1,31))

for i in range(28):
    num = int(input())
    student.remove(num)

student.sort()

print(student[0])
print(student[1])