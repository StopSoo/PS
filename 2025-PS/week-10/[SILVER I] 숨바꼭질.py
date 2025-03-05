# https://www.acmicpc.net/problem/1697

# 내 답안
# 걸린 시간: 180ms
# 1시간 푼 듯 ... 그래도 BFS를 이용한다는 걸 알아서 풀 수 있었음 !!
# 다른 사람들 답안 찾아보니까 다들 비슷함 !!
from collections import deque

N, K = map(int, input().split())
dt = dict()
dt[0] = [1]
dt[1] = [0, 2]
for i in range(2, 100001): dt[i] = [i-1, i+1, i*2]

def bfs(n):
  global dt, checked

  q = deque()
  q.append((n, 0))
  checked[n] = True

  while q:
    node = q.popleft()
    if node[0] == K:
      print(node[1]) # depth 출력
      break
    for neighbor in dt[node[0]]:
      if neighbor > 100000 or checked[neighbor]: continue # N의 최댓값 10만
      q.append((neighbor, node[1] + 1)) # 깊이를 같이 추가
      checked[neighbor] = True

checked = [False for _ in range(100001)]
bfs(N)