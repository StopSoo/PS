# https://www.acmicpc.net/problem/2580

# 답안
# 걸린 시간: 2404ms
# 일단 한 1시간 정도 푼 것 같음
# 3x3 구역을 탐색하는 방법을 구현하기가 어려웠음
def is_possible(y, x, n):
  global matrix

  for c in range(9): # 행 탐색
    if matrix[y][c] == n: return False
  for r in range(9): # 열 탐색
    if matrix[r][x] == n: return False
  for r in range(3): # 3x3 탐색 (!)
    for c in range(3):
      if matrix[3*(y//3) + r][3*(x//3) + c] == n: return False
  
  return True

def search(lev):
  global pos, matrix

  if lev == len(pos): # 스도쿠 완성
    for i in range(9):
      for j in range(9):
        print(matrix[i][j], end=' ')
      print()
    exit(0)
    return
  
  y, x = pos[lev] # 0인 지점 추출

  for n in range(1, 10):
    if is_possible(y, x, n):
      matrix[y][x] = n
      search(lev + 1)
      matrix[y][x] = 0

matrix = [list(map(int, input().split())) for _ in range(9)]

pos = [] # 0인 위치의 x,y좌표 넣기 
for i in range(9):
  for j in range(9):
    if matrix[i][j] == 0: pos.append((i, j))

search(0) # 0번째 빈칸부터 탐색