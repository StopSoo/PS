# https://www.acmicpc.net/problem/5567

# 내 답안
# 걸린 시간: 64ms
# 알고리즘: 그래프 탐색
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input()) # 동기의 수 
m = int(input()) # 리스트의 길이
graph = defaultdict(list)
for _ in range(m):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

deq = deque([(1, 0)]) # (now, depth) 
checked = [0] * (n + 1)
checked[1] = 1 # 상근 체크
while deq:
  now, depth = deq.popleft()
  
  if depth <= 1:
    for friend in graph[now]:
      if not checked[friend]:
        checked[friend] = True
        deq.append((friend, depth + 1))

print(sum(checked) - 1) # 자기 제외