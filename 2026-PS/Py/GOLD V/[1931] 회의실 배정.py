# https://www.acmicpc.net/problem/1931
# 260120 풀이
# 알고리즘: 그리디 / 정렬
# 시간: 256ms

# 내 답안
# 탐욕적 선택 속성을 활용한 "종료 시간이 이른 것, 종료 시간이 같다면 시작 시간이 이른 것" 기준으로 정렬!
import sys
input = sys.stdin.readline

N = int(input().strip())
times = sorted([list(map(int, input().strip().split())) for _ in range(N)], key=lambda x: [x[1], x[0]]) # 정렬 조건 설정할 때 "key="

count = 1 # 첫 번째로 끝나는 회의 선택
end_time = times[0][1]
for s, e in times[1:]:
    if s >= end_time:
        end_time = e
        count += 1

print(count)