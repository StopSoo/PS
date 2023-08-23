# 2693 : N번째 큰 수
import sys
input = sys.stdin.readline

num = int(input())  # 테스트 케이스의 개수 입력 받기

for _ in range(num):
    array = list(map(int, input().split(' ')))
    array.sort(reverse=True)
    print(array[2])

# 형 변환 - map을 통해서 !!
# 정렬 내림차순 - sort에서 'reverse' 조건 적용 !!