# num1 = int(input("input number1: "))
# num2 = int(input("input number2: "))
# num3 = int(input("input number3: "))

lst = []
for i in range(1, 4):
    lst.append(int(input(f"input number{i}: ")))

print(max(lst))