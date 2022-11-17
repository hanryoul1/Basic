pos = input("우편번호: ")
num = int(pos[2])

if 0 <= num <= 2:
    print("강북구")

elif 3 <= num <= 5:
    print("도봉구")

else:
    print("노원구")