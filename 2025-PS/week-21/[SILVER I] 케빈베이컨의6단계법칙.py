# https://www.acmicpc.net/problem/1389

# 내 답안
# 걸린 시간: 232ms -> BFS / 다익스트라보다는 오래 걸림 (모든 노드에 대해 구하므로)
# 알고리즘: 플로이드-워셜
N, M = map(int, input().split())
matrix = [[N] * N for _ in range(N)] # INF를 N으로 표현
for _ in range(M):
  a, b = map(int, input().split())
  matrix[a-1][b-1] = matrix[b-1][a-1] = 1 # 연결된 노드끼리 거리는 1

for i in range(N): # 대각선은 0으로 설정
  matrix[i][i] = 0 

for k in range(N):
  for i in range(N):
    for j in range(N):
      if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]

result = []
for row in matrix:
  result.append(sum(row))
print(result.index(min(result)) + 1)