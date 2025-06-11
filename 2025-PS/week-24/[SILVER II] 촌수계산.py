# https://www.acmicpc.net/problem/2644

# 내 답안
# 걸린 시간: 56ms
# 알고리즘: BFS
# 보완한 부분: BFS의 특성 상 처음 목적지에 도달했을 때 count가 최소이기 때문에 계속해서 반복문을 돌릴 필요가 없음.
import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n = int(input())
graph = defaultdict(list)
a, b = map(int, input().strip().split())
m = int(input())
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n + 1)
deq = deque([(a, 0)])
visited[a] = True
while deq:
  now, count = deq.popleft()
  if now == b: # 목적지에 도달한 경우
    print(count)
    break
  
  for neighbor in graph[now]:
    if not visited[neighbor]:
      visited[neighbor] = True
      deq.append((neighbor, count + 1))
else: # 목적지에 도달하지 못한 경우
  print(-1)