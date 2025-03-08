# https://www.acmicpc.net/problem/7576

# 내 답안
# 걸린 시간: 2280ms
# 푸는 데 30분 정도 걸린 듯 ! 근데 시간 초과 해결하는 게 또 30분 ....
# 디버깅할 때 헤맨 점: =를 ==로 적어놓은 부분 (;;)
# all(리스트) 함수: 리스트 내 모든 값들이 True인지를 반환
# 시간 초과를 해결하기 위해 크게 수정했어야 하는 부분
# 1) 배열 내 0 패딩 없애고 인덱스도 0부터로 수정
# 2) 방문 배열 굳이 하나 더 만들지 말고, 본 배열로 체크
# 3) all() 함수 사용 시 행, 열 다 돌지 말고 하나만 돌아서 O(N)으로 사용할 것
from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

M, N = map(int, input().strip().split())
tomatoes = [list(map(int, input().strip().split())) for _ in range(N)]

deq = deque()
max_day = 0

for i in range(N):
  for j in range(M):
    if tomatoes[i][j] == -1: # 토마토가 없는 곳은 아예 방문 체크해놓기 (-1을 1로 변경)
      tomatoes[i][j] = 1
    elif tomatoes[i][j] == 1: # 처음에 토마토가 있는 곳들만 덱에 넣기
      deq.append((i, j, 0))

while deq:
  y, x, day = deq.popleft()
  max_day = day

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < N and 0 <= nx < M) and (tomatoes[ny][nx] == 0):
      deq.append((ny, nx, day+1))
      tomatoes[ny][nx] = 1 # 방문 체크

flag = any(0 in row for row in tomatoes) # O(N)
print(max_day if not flag else -1)