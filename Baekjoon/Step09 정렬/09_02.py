# sort 함수: 리스트명.sort( ) 형식으로 "리스트형의 메소드"​​이며 리스트 원본값을 직접 수정
# sorted 함수: sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환

"""
lst = []

n = int(input())

for j in range(n):
    num = int(input())
    lst.append(num)

lst.sort()

for i in range(n):
    print(lst[i])
"""

N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))
    
nums = sorted(nums)

for i in range(N):
    print(nums[i])