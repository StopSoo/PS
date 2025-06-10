# https://www.acmicpc.net/problem/10830

# 내 답안
# 걸린 시간: 44ms
# 알고리즘: 분할 정복
# 1. matmul() -> 누적 시마다 모듈러 연산을 해주는 게 좋다! (오버플로우 방지)
# 2. power() -> 
import sys
sys.setrecursionlimit(1000000)

def matmul(A, B): # 행렬 A와 행렬 B의 곱셈 연산을 하는 함수
  matrix = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        matrix[i][j] += A[i][k] * B[k][j]
        matrix[i][j] %= 1000
  return matrix

def power(A, B): # A행렬의 B제곱을 구하는 함수
  if B == 1: # 무한 재귀 방지 처리 필수 (!)
    return [[element % 1000 for element in row] for row in A]

  if B % 2 == 1:
    return matmul(A, power(A, B - 1))
  else:
    half = power(A, B // 2)
    return matmul(half, half)

N, B = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
result = power(matrix, B)
for row in result:
  print(*row)