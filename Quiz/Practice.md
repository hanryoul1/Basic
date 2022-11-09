[02.py]
<random 함수>
random() : 0 ~ 10 미만의 임의의 값 생성
randrange(1, 46) : 1 ~ 46 미만의 임의의 값 생성
randint(1, 45) : 1 ~ 45 이하의 임의의 값 생성


[03.py]
<문자열 포맷>
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아합니다." % "파이썬")
print("Apple은 %c로 시작합니다." % "A")
print("나는 %s색과 %s색을 좋아합니다." % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아합니다.".format(age = 20, color = "빨간"))

age = 20, color = "빨간" 
print(f"나는 {age}살이며, {color}색을 좋아합니다.")


[04.py]
<list>
list = []
dictionary = {key : value}
tuple = ( , )  // 내용 변경 및 추가 불가능
set = {}  // 중복, 순서 없음


[10.py]
<내장함수>
input : 사용자 입력을 받는 함수
dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는 표시하는 함수

<외장함수>
glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))

datetime : 날짜 관련 함수
import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days = 100) # 100일 뒤 날짜 저장
print("우리가 만난지 100일은", today + td)