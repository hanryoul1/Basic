# 296.py
# 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러 발생
# 에러가 발생하는 PER은 0으로 출력

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)