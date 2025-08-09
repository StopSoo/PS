# https://www.acmicpc.net/problem/2615

# 내 답안
# 걸린 시간: 틀렸습니다
# 알고리즘: 구현
# 첫 코드의 문제점 1) 6개를 초과하는지를 체크할 때 변수 범위를 잘 지정할 것.
# 첫 코드의 문제점 2) 하드코딩이라 유지보수성이 떨어짐.
import sys
input = sys.stdin.readline

gamepan = list(list(map(int, input().strip().split())) for _ in range(19))

def check(dir, r, c, color):
  if dir == 1: # 아래쪽 직진
    if r <= 14 and all(gamepan[r+a][c] == color for a in range(5)): 
      if (1 <= r and gamepan[r+5][c] != color and gamepan[r-1][c] != color) or r == 0: # 5개를 초과했는지 체크
        return [r+1, c+1]
  elif dir == 2: # 오른쪽 직진
    if c <= 14 and all(gamepan[r][c+a] == color for a in range(5)): 
      if (1 <= c and gamepan[r][c+5] != color and gamepan[r][c-1] != color) or c == 0:
        return [r+1, c+1]
  elif dir == 3: # 오른쪽 아래 대각선
    if r <= 14 and c <= 14 and all(gamepan[r+a][c+a] == color for a in range(5)):
      if (1 <= r and 1 <= c and gamepan[r+5][c+5] != color and gamepan[r-1][c-1] != color) or r == 0 or c == 0:
        return [r+1, c+1]
  else: # 오른쪽 위 대각선
    if r >= 4 and c <= 14 and all(gamepan[r-a][c+a] == color for a in range(5)):
      if (r <= 13 and 5 <= c and gamepan[r-5][c+5] != color and gamepan[r+1][c-1] != color) or r == 18 or c == 0:
        return [r+1, c+1]
  
  return [-1, -1]

winner = 0
res = [-1, -1]
found = False # 탈출 플래그
for r in range(19):
  for c in range(19):
    if found: break
    if gamepan[r][c] == 1: # 검정 말의 경우
      for i in range(1, 5):
        res = check(i, r, c, 1)
        if res != [-1, -1]:
          winner = 1
          found = True
          break
    elif gamepan[r][c] == 2: # 흰 말의 경우
      for i in range(1, 5):
        res = check(i, r, c, 2)
        if res != [-1, -1]:
          winner = 2
          found = True
          break
if not found: print(0)
else:
  print(winner)
  print(*res)

# 정답 코드
# 걸린 시간: 36ms
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
directions = [(1,0), (0,1), (1,1), (-1,1)]  # 아래, 오른쪽, 오른쪽아래, 오른쪽위

def dfs(r, c, dr, dc, color, cnt):
  nr, nc = r + dr, c + dc
  if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color:
    return dfs(nr, nc, dr, dc, color, cnt+1)
  return cnt

def check(r, c, dr, dc, color):
  # 이전 칸이 같은 색이면 중복 시작점(!!!!)
  pr, pc = r - dr, c - dc
  if 0 <= pr < 19 and 0 <= pc < 19 and board[pr][pc] == color:
    return False
  # 연속 개수 세기
  length = dfs(r, c, dr, dc, color, 1)
  return length == 5

winner = 0
res = []
found = False
for r in range(19):
  for c in range(19):
    if board[r][c] != 0:
      color = board[r][c]
      for dr, dc in directions:
        if check(r, c, dr, dc, color):
          winner = color
          res = [r + 1, c + 1]
          found = True
          break
    if found: break
  if found: break

if not found: print(0)
else:
  print(winner)
  print(*res)
