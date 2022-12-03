# 294.py
# '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장

f = open("C:/Users/한률/Desktop/VSC/Basic/Beginner/12 파일 입출력과 예외처리/매수종목1.txt", encoding = "utf-8")
lines = f.readlines() # python list

codes = []
for line in lines:
    code = line.strip() 
    # 문자열의 앞 뒤에 공백과 줄바꿈 문자가 있을 때 strip()을 사용하여 모두 제거
    # '\n'
    print(code)
    codes.append(code)

print(codes)

f.close()