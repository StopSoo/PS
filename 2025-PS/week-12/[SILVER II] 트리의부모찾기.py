# https://www.acmicpc.net/problem/11725

# 내 답안
# 걸린 시간: 388ms
# BFS로 풀이 (!) 트리에 익숙해지자 ~~
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
answer = [0] * (N+1) # 제출할 정답 (부모 노드)
graph = dict()
for _ in range(N-1): # 그래프 만들기
  s, e = map(int, input().strip().split())
  graph[s] = graph.get(s, []) + [e]
  graph[e] = graph.get(e, []) + [s]

deq = deque([1])
visited = [False] * (N+1)
while deq:
  node = deq.popleft()
  visited[node] = True
  for ele in graph[node]:
    if not visited[ele]:
      answer[ele] = node
      deq.append(ele)

print(*answer[2:], sep='\n')