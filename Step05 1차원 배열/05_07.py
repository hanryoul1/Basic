cnt = int(input())  # 테스트 케이스의 개수

for i in range(cnt):
    num_list = list(map(int, input().split()))  # 학생의 수 N, 이어서 N명의 점수
    mid = sum(num_list[1:])/num_list[0]  # 평균 점수
    student = 0

    for j in num_list[1:]:
        if j > mid:
            student += 1
    
    result = student/num_list[0]*100
    print(f'{result:.3f}%')