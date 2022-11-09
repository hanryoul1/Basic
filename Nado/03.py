"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) https://naver.com
규칙 1) https:// 부분은 제외 => naver.com
규칙 2) 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3) 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"로 구성(!)

출력 결과 ) nav51!
"""

# Solution_MY
site = str(input())
first = site[8:]
second = first[:(first.index("."))]
third = second[:3] + str(len(second)) + str(second.count('e')) + '!'
print(third)

# Solution
url = "https://naver.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)