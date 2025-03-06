# https://www.acmicpc.net/problem/12865

# 내 답안
# 걸린 시간: 6024ms
# Bottom-Up 방식으로 구현. 하지만 이 문제는 Top-Down 방식이 더 효율적.(DP 테이블을 완성해야 하는 것은 아님)
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
infos = [[0, 0]] + [list(map(int, input().strip().split())) for _ in range(N)] # [무게, 가치]
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, K+1):
    dp[i][j] = dp[i-1][j] 
    if j - infos[i][0] >= 0: # 현재 원소를 확실히 선택한 경우와 비교
      dp[i][j] = max(dp[i][j], dp[i-1][j-infos[i][0]] + infos[i][1])

print(dp[N][K])