"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

표준 체중 : 각 개인의 키에 적당한 체중
남성 : 키(m) * 키(m) * 22
여성 : 키(m) * 키(m) * 21

조건 1) 표준 체중은 별도의 함수 내에서 계산 / 함수명 : std_weight / 전달값 : 키(height), 성별(gender)
조건 2) 표준 체중은 소수점 둘째까지까지 표시

출력 결과 ) 키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

# Solution_MY
def std_weight(height, gender):
    weight = 0
    
    if gender == "남성":
        weight = round((height / 100) * (height / 100) * 22, 2)
        print(f"키 {height}cm {gender}의 표준 체중은 {weight} 입니다.")
        return weight
    
    elif gender == "여성":
        weight = round((height / 100) * (height / 100) * 21, 2)
        print(f"키 {height}cm {gender}의 표준 체중은 {weight} 입니다.")
        return weight

std_weight(175, "남성")

# Solution
def std_weight(height, gender):
    if gender == "남성":
        return height * height * 22

    else:
        return height * height * 21
    
height = 175
gender = "남성"
weight = round(std_weight(height / 100, gender), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")