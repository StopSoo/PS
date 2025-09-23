# https://www.acmicpc.net/problem/2170

# 내 답안
# 걸린 시간: 3952ms
# 알고리즘: 정렬 / 스위핑
import sys
input = sys.stdin.readline

N = int(input().strip())
lines = []
for _ in range(N):
  s, e = map(int, input().strip().split())
  lines.append([s, e])

lines.sort() # 정렬이 포인트 (!)

answer = 0 # 선의 총 길이
start, end = lines[0]
for x, y in lines[1:]:
  if end < x: # 갱신 필요
    answer += (end - start)
    start, end = x, y
  else: # 합쳐짐
    end = max(end, y)
answer += (end - start)

print(answer)