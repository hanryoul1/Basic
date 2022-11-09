a = int(input())
b = int(input())

one = a
two = b
three = a * (b % 10)
four = a * (b % 100 //10)
five = a * (b // 100)
six = a * b

print(three)
print(four)
print(five)
print(six)