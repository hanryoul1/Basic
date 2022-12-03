# 297.py
# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장

per = ["10.31", "", "8.00"]
lst = []

for i in per:
    try:
        i = float(i)
    except:
        i = 0
        
    lst.append(i)

print(lst)