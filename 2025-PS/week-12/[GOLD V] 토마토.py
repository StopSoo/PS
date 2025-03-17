# https://www.acmicpc.net/problem/7569

# 내 답안
# 걸린 시간: 2716ms 
# 푸는 데는 25분 정도 걸린 듯 !!
# 체크 1) 3차원 배열에서 all() 함수 사용하는 방법 체크하기.
# 체크 2) 반복문 3번 쓰는 것보다 리스트 컴프리헨션을 사용하는 것이 더 깔끔하고 가독성 있음 (!)
# 체크 3) 시작할 때부터 토마토가 모두 익어있었을 경우를 따로 flag로 체크하지 않고, max_day가 0인 경우로 바로 체크 (!)
from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
dh = [1, -1]
# flag = False

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # MxNxH 토마토 박스
# if not any(x == 0 for floor in tomatoes for row in floor for x in row): flag = True

# for h in range(H):
#   for i in range(N):
#     for j in range(M):
#       if tomatoes[h][i][j] == -1: # 토마토가 없는 곳은 1로 변경해서 방문 체크 해놓기
#         tomatoes[h][i][j] = 1
#       elif tomatoes[h][i][j] == 1:
#         deq.append((h, i, j, 0)) # 마지막은 일 수
deq = deque([(h, i, j, 0) for h in range(H) for i in range(N) for j in range(M) if tomatoes[h][i][j] == 1]) # 리스트 컴프리헨션 (!)
total_unripe = sum(1 for floor in tomatoes for row in floor for x in row if x == 0) # 안 익은 토마토의 개수 체크 
max_day = 0

while deq:
  h, y, x, day = deq.popleft()
  max_day = day

  for i in range(4): # 동서남북
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < N and 0 <= nx < M) and (tomatoes[h][ny][nx] == 0):
      tomatoes[h][ny][nx] = 1
      total_unripe -= 1
      deq.append((h, ny, nx, day+1))
  for i in range(2): # 상하
    nh = h + dh[i]
    if (0 <= nh < H) and (tomatoes[nh][y][x] == 0):
      tomatoes[nh][y][x] = 1
      total_unripe -= 1
      deq.append((nh, y, x, day+1))
# if all(x == 1 for floor in tomatoes for row in floor for x in row): # 토마토가 모두 1이라면
if total_unripe == 0:
  print(max_day)
else: # 모두 익지는 못한다면
  print(-1)