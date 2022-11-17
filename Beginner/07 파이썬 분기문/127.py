# Solution_MY
me = input("주민등록번호: ")
num = int(me[7])

if num == 1 or num == 3:
    print("남자")

elif num == 2 or num == 4:
    print("여자")

# Solution
me = input("주민등록번호: ")
num = me.split("-")[1] # ['011228', '4123456']

if num[0] == "1" or num[0] == "3":
    print("남자")

else:
    print("여자")