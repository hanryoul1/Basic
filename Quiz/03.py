"""
문자열 포맷

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

"""

"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) https://naver.com
규칙 1) https:// 부분은 제외 => naver.com
규칙 2) 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3) 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"로 구성(!)

출력 결과 ) nav51!
"""

site = str(input())
first = site[8:]
second = first[:(first.index("."))]
third = second[:3] + str(len(second)) + str(second.count('e')) + '!'
print(third)

url = "https://naver.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)