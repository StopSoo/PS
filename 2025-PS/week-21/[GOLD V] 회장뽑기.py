# https://www.acmicpc.net/problem/2660

# 내 답안
# 걸린 시간: 64ms
# 알고리즘: 플로이드-워셜
# 처음에 틀렸습니다 나왔을 때 간과한 것 -> INF가 아닐 때(이미 초기화한 곳)는 continue한 것 !! (먼저 초기화한 값이 최단경로값이라는 보장이 없음)
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
INF = int(1e9)
matrix = [[INF] * (N + 1) for _ in range(N + 1)] # 1기반 인덱스
for i in range(1, N + 1): matrix[i][i] = 0 # 대각선은 0 처리
while True:
  a, b = map(int, input().strip().split())
  if a == -1 and b == -1: break
  # 친구 사이니까 1
  matrix[a][b] = 1 
  matrix[b][a] = 1

for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]

score = [0] * (N + 1) # 1기반 인덱스
for i in range(1, N + 1):
  score[i] = max(matrix[i][1:]) # 친구 사이 점수 책정

max_score = min(score[1:]) # 점수가 가장 작은 사람이 회장
max_count = score.count(max_score)
max_values = [i for i, s in enumerate(score) if s == max_score]
print(max_score, max_count)
print(*max_values)