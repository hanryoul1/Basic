# 241.py
# datetime 
import datetime
now = datetime.datetime.now()
print(now)

# 242.py
# datetime 
print(now, type(now))

# 243.py
# datetime 
for day in range(5, 0, -1):
    delta = datetime.timedelta(days = day)
    date = now - delta
    print(date)

# 244.py
# datetime & strftime
# strftime: 날짜와 시간(datetime)을 문자열로 출력
print(now.strftime("%H:%M:%S"))

# 245.py
# datetime & strptime
# strptime: 날짜와 시간 형식의 문자열을 datetime으로 변환
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246.py
# time & sleep
# datetime
import time
import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247.py
# 모듈을 임포트하는 4가지 방식
# Pass

# 248.py
# os & getcwd
import os
ret = os.getcwd()
print(ret, type(ret))

# 249.py
# os & rename
# os.rename("C:/Users/한률/Desktop/before.txt", "C:/Users/한률/Desktop/after.txt")

# 250.py
# numpy & arange
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)