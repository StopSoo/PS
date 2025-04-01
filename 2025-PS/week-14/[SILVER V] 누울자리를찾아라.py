# https://www.acmicpc.net/problem/1652

# 내 답안
# 걸린 시간: 40ms
# 처음에 문제를 잘못 이해해서 틀렸음. 놓친 부분 -> 짐까지만 뻗음. 같은 열/행에서 짐 뒤 영역도 체크해야 함.
import sys
input = sys.stdin.readline

N = int(input().strip())
room = [input().strip() for _ in range(N)]
visited_row = [False]*N # 행 방문 체크
visited_col = [False]*N # 열 방문 체크

row, col = 0, 0
for y in range(N):
  for x in range(N):
    if room[y][x] == '.': # 오른쪽과 아래만 체크
      if 0 <= y+1 < N and room[y+1][x] == '.' and not visited_col[x]:
        col += 1
        visited_col[x] = True
      if 0 <= x+1 < N and room[y][x+1] == '.' and not visited_row[y]:
        row += 1
        visited_row[y] = True
    elif room[y][x] == 'X': # 짐이라면
      visited_row[y] = False
      visited_col[x] = False

print(row, col)