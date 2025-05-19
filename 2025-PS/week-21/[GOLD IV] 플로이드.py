# https://www.acmicpc.net/problem/11404

# 내 답안
# 걸린 시간: 420ms
# 알고리즘: 플로이드-워셜 (모든 점-모든 점)
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

matrix = [[INF] * (N+1) for _ in range(N+1)] # 1기반 인덱스
for i in range(1, N+1): matrix[i][i] = 0 # 대각선은 0으로 처리
for _ in range(M):
  s, e, w = map(int, input().strip().split())
  matrix[s][e] = min(matrix[s][e], w)

for k in range(1, N+1): # 거쳐가는 노드
  for i in range(1, N+1): # 시작
    for j in range(1, N+1): # 도착
      if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(1, N+1):
  for j in range(1, N+1):
    if matrix[i][j] != INF: print(matrix[i][j], end=' ')
    else: print(0, end=' ') # 갈 수 없는 곳은(갱신되지 않은 곳은) 0으로 처리
  print()