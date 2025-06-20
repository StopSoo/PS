# https://www.acmicpc.net/problem/18352

# 내 답안
# 걸린 시간: 1648ms
# 알고리즘: BFS
import sys
input = sys.stdin.readline
from collections import defaultdict, deque  

N, M, K, X = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b)

deq = deque([(X, 0)])
answer = []
visited = [False] * (N + 1)
visited[X] = True
while deq:
  node, dist = deq.popleft()
  if dist == K: answer.append(node)
  
  for neighbor in graph[node]:
    if not visited[neighbor] and dist < K:
      visited[neighbor] = True       
      deq.append((neighbor, dist + 1))
  
print('\n'.join(map(str, sorted(answer))) if answer else -1)

# 알고리즘: 다익스트라
# 우선순위 큐 써서 시간복잡도를 줄이자 !!!!!!!!!!
# 걸린 시간: 2468ms
import sys, heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
INF = 1e8

graph = [[] for _ in range(N+1)] # 1번 노드부터 시작
distance = [INF] * (N+1) # 거리 배열

for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (우선순위, 값)
  distance[start] = 0 # 시작 노드는 0으로 초기화

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue   

    for neighbor in graph[now]:
      if dist + 1 < distance[neighbor]:
        distance[neighbor] = dist + 1 # 갱신
        heapq.heappush(q, (dist + 1, neighbor))

dijkstra(X)
if all(x != K for x in distance[1:]): print(-1)
else:
  for i in range(1, N+1):
    if distance[i] == K: 
      print(i)