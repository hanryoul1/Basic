# 299.py
# 예외 발생 시 에러 메시지를 변수로 바인딩

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as msg: # IndexError: list index out of range
        print(msg)