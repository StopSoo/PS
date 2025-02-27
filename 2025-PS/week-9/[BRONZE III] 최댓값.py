# https://www.acmicpc.net/problem/2566

# 내 답안
# 걸린 시간: 32ms
mx, i, j = 0, 0, 0
maze = [list(map(int, input().split())) for _ in range(9)]
for irow, row in enumerate(maze):
  for icol, cell in enumerate(row):
    if cell > mx: 
      mx = cell
      i, j = irow, icol
print(mx)
print(i+1, j+1)