# https://www.acmicpc.net/problem/2170
# 260121 풀이
# 알고리즘: 정렬 / 스위핑
# 시간: 4488ms

import sys
input = sys.stdin.readline

N = int(input().strip())
lines = [list(map(int, input().strip().split())) for _ in range(N)]

lines.sort() # 정렬이 포인트!

answer = 0 # 선의 총 길이 
start, end = lines[0];
for s, e in lines[1:]:
    if end < s: # 갱신 필요
        answer += (end - start)
        start, end = s, e
    else: # 기존 선에 일부 or 전체가 합쳐짐
        end = max(end, e)
answer += (end - start)
print(answer)