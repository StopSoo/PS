# https://www.acmicpc.net/problem/1987

# 내 답안
# 걸린 시간: 6104ms (pypy3)
# 백트래킹: 답이 될 수 없는 경우는 제외하고 탐색.
# set() 사용 시 -> 원하는 값 제거는 remove(값) 사용하기
import sys
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def count_colors(y, x):
  global dy, dx, R, C, colors, alphas, answer

  answer = max(len(alphas), answer) # 정답 업데이트

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < R and 0 <= nx < C) and (colors[ny][nx] not in alphas):
      alphas.add(colors[ny][nx])
      count_colors(ny, nx) # 재귀
      alphas.remove(colors[ny][nx]) # 해당 값 제거

R, C = map(int, input().strip().split())
colors = [input() for _ in range(R)]
alphas = set() # 지나온 알파벳들을 담을 집합 -> 어차피 겹치지 않을 거니까 시간복잡도가 더 낮은 set을 사용(!)
alphas.add(colors[0][0]) # 시작점 알파벳 추가

answer = 0
count_colors(0, 0)
print(answer)

# 강의에서 나온 코드 (python으로 시간 초과 뜸)
# 시간 초과 해결 방안: 알파벳 체크 여부를 if board[y][x] in st가 아닌 체크 배열을 사용해서 O(1)의 시간복잡도로 바꾸기 (!)
def search(y, x):
  global dy, dx, R, C, board, st, ans

  if y < 0 or x < 0 or y >= R or x >= C: return
  if board[y][x] in st: return
  
  st.add(board[y][x])

  ans = max(ans, len(st))

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    search(ny, nx)
  
  st.remove(board[y][x])

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

st = set()
ans = 0

search(0, 0)
print(ans)

# 최종 답안 (얘도 pypy3로 통과)
# 걸린 시간: 3724ms
# in을 사용하지 않고, 체크 배열을 사용 (!)
def search(y, x):
  global dy, dx, R, C, board, check, cur_len, ans

  if y < 0 or x < 0 or y >= R or x >= C: return
  if check[ord(board[y][x]) - 65]: return
  
  check[ord(board[y][x]) - 65] = True
  cur_len += 1

  ans = max(ans, cur_len)

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    search(ny, nx)
  
  cur_len -= 1
  check[ord(board[y][x]) - 65] = False

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

check = [False] * 26
cur_len = 0
ans = 0

search(0, 0)
print(ans)