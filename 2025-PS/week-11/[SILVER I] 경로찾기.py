# https://www.acmicpc.net/problem/11403

# 내 답안
# 걸린 시간: 140ms
from collections import deque

def bfs(start, end):
  global N, dt

  flag = False
  visited = [False] * N
  deq = deque()
  deq.append((start, end))

  while deq:
    s, e = deq.popleft()
    visited[s] = True
    for node in dt[s]:
      if not visited[node]:
        if node == e:
          flag = True
          break
        else: deq.append((node, end))
      else: # 방문은 했지만 시작점으로 돌아온 경우
        if node == end:
          flag = True
          break
    if flag: break # 첫 코드 제출 때 놓친 부분 (!)

  if flag: return True
  else: return False


N = int(input())
dt = dict()
for i in range(N): dt[i] = [] # 딕셔너리 초기화

graph = [list(map(int, input().split())) for _ in range(N)]
for row_num, row in enumerate(graph): # 인접 리스트 만들기
  for idx, e in enumerate(row):
    if e == 1: dt[row_num] += [idx]

answer = [[0] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if bfs(i, j) == True: answer[i][j] = 1
    else: answer[i][j] = 0
# 최종 출력
for i in range(N):
  print(*answer[i])