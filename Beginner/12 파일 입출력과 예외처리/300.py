# 300.py

"""
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
"""

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("예외가 발생하지 않았습니다.")
    finally:
        print("문세희 잔다.")

"""
10.31
예외가 발생하지 않았습니다.
문세희 잔다.
0
문세희 잔다.
8.0
예외가 발생하지 않았습니다.
문세희 잔다.
"""