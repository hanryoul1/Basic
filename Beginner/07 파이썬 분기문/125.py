number = input("휴대전화 번호 입력: ")
N = number[:3]

if N == "011":
    print("당신은 SKT 사용자입니다.")
elif N == "016":
    print("당신은 KT 사용자입니다.")
elif N == "019":
    print("당신은 LGU 사용자입니다.")
else:
    print("이 번호는 알 수 없는 번호입니다.")