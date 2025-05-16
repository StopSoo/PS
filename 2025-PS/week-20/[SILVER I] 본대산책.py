# https://www.acmicpc.net/problem/12849

# 답안
# 걸린 시간: 932ms
# 알고리즘: 그래프 + DP
# 단순히 BFS를 쓰기엔 메모리 초과가 남.
from collections import defaultdict

graph = defaultdict(list)
for x, y in [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,7),(6,7)]:
  graph[x].append(y)
  graph[y].append(x)

N = int(input()) # 산책 시간
dp = [[0] * 8 for _ in range(N+1)] # 시간마다 i번 노드에 도달하는 경우의 수 
dp[0][0] = 1 # 시작 지점

for t in range(N): # 시간
  for i in range(8): # 노드
    for neighbor in graph[i]:
      dp[t+1][neighbor] = (dp[t+1][neighbor] + dp[t][i]) % 1000000007

print(dp[N][0])