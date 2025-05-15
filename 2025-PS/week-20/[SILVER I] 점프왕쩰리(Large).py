# https://www.acmicpc.net/problem/16174

# 내 답안 1
# 걸린 시간: 60ms
# 알고리즘: BFS
# 첫 코드 때 시간 초과 난 원인 -> 방문 체크 안 해서 ,, (안 해도 될 거라고 생각함)
# 그리고 좀 더 복잡도를 줄일 수 있었던 부분 -> deq에 넣을 때 y, x 좌표만 넣기 (!)
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
gamepan = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)] # 방문 체크 배열

deq = deque()
deq.append((0, 0))
visited[0][0] = True
while deq:
  y, x = deq.popleft()
  jump = gamepan[y][x]

  if jump == -1: # 도착 지점에 도달
    print("HaruHaru")
    break

  for i in range(2):
    ny, nx = y + (jump * i), x + (jump * (1 - i))
    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]: # 범위 안이고 방문하지 않았으면
      visited[ny][nx] = True # 방문 체크
      deq.append((ny, nx))
else: print("Hing")

# 내 답안 2
# 자료구조: 힙
# 걸린 시간: 48ms
import sys, heapq
input = sys.stdin.readline

N = int(input())
gamepan = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)] # 방문 체크 배열

q = []
heapq.heappush(q, (-gamepan[0][0], 0, 0)) # jump 값이 큰 순서대로 해보기
while q:
  jump, y, x = heapq.heappop(q)
  if gamepan[y][x] == -1: # 도착 지점에 도달
    print("HaruHaru")
    break
  
  jump = -jump # 다시 값 복구
  for i in range(2):
    ny, nx = y + (jump * i), x + (jump * (1 - i))
    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]: # 범위 안이면
      visited[ny][nx] = True # 방문 체크
      heapq.heappush(q, (-gamepan[ny][nx], ny, nx))
else: print("Hing")

# DP로 푼다면?
# 걸린 시간: 36ms (세 방법 중 제일 빠름 !!)
# 도달 가능 여부 기록이 포인트이기 때문에, 굳이 DP로 풀 필요는 없음!
import sys
input = sys.stdin.readline

N = int(input())
gamepan = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[False] * N for _ in range(N)]
dp[0][0] = True

for y in range(N):
  for x in range(N):
    if dp[y][x]:
      jump = gamepan[y][x]

      if jump == -1: continue
      if y + jump < N:
        dp[y + jump][x] = True
      if x + jump < N:
        dp[y][x + jump] = True

if dp[N-1][N-1]: print("HaruHaru")
else: print("Hing")