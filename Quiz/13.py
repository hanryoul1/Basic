"""
Quiz) "사회적 거리두기"에 따른 영화관 좌석 예매 시스템을 만드시오

조건 1) 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성
        EX. A1 ~ A20, B1 ~ B20, C1 ~ C20

조건 2) 이때 A열에 대해서 홀수로 끝나는 좌석에 대해서만 출력 (각 좌석은 " "로 구분)
        EX. A1 A3 A5 A& ... A19
"""

# Solution_MY
seats = []
alphabet = ["A", "B", "C"]

for a in alphabet:
    for n in range(1, 21):
        if n % 2 != 0:
            print(a + str(n), end = " ")

# Solution
for i in range(1, 21)[::2]: # 2칸씩 건너 뛰어서
    #if i % 2 == 1:
        print("A" + str(i), end = " ")