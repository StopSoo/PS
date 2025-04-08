# https://www.acmicpc.net/problem/2002

# 내 답안
# 걸린 시간: 2232ms
import sys
input = sys.stdin.readline

N = int(input().strip())
in_car = list(input().strip() for _ in range(N))
dt = dict()
for i in range(N): # 앞에 있는 차들을 딕셔너리로 정리하기
  if i == 0:
    dt[in_car[0]] = []
  for j in range(i):
    dt[in_car[i]] = dt.get(in_car[i], []) + [in_car[j]]
out_car = list(input().strip() for _ in range(N))

count = 0
for i, car_name in enumerate(out_car):
  if len(dt[car_name]) > i:
    count += 1
  elif len(dt[car_name]) <= i:
    for car in dt[car_name]:
      if car not in out_car[:i]:
        count += 1
        break

print(count)

# deque를 활용해 더 시간복잡도가 낮은 답안
# 걸린 시간: 56ms
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
enter = deque([input().rstrip() for _ in range(n)])
out = deque([input().rstrip() for _ in range(n)])
visited = set()
cnt = 0

for car in out:
  print(enter)
  print(visited)
  while enter and enter[0] in visited:
    enter.popleft()
  if enter and car != enter[0]:
    cnt += 1
    visited.add(car)
  else:
    enter.popleft()

print(cnt)