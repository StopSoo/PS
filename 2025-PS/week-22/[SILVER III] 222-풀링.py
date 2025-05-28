# https://www.acmicpc.net/problem/17829

# 내 답안
# 걸린 시간: 468ms
import sys
input = sys.stdin.readline 

def pooling(n, matrix):
  new_matrix = [[0] * (n // 2) for _ in range(n // 2)]
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      new_matrix[i//2][j//2] = sorted([matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]])[-2]
  return new_matrix

N = int(input())
matrix = list(list(map(int, input().split())) for _ in range(N))

answer = pooling(N, matrix)
while N != 2:
  answer = pooling(N//2, answer)
  N //= 2
print(answer[0][0])

# 좀 더 분할정복 형태로 정리한 코드
# 걸린 시간: 440ms
import sys
input = sys.stdin.readline

def pooling(x, y, size): # (x, y): 시작점 size: 정사각형 크기
  if size == 2:
    nums = [
      matrix[x][y], matrix[x][y+1],
      matrix[x+1][y], matrix[x+1][y+1]
    ]
    return sorted(nums)[-2]
  
  half = size // 2
  values = [
    pooling(x, y, half),
    pooling(x, y + half, half),
    pooling(x + half, y, half),
    pooling(x + half, y + half, half)
  ]
  return sorted(values)[-2]

N = int(input())
matrix = list(list(map(int, input().split())) for _ in range(N))

print(pooling(0, 0, N))