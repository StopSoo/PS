# https://www.acmicpc.net/problem/14430

# 내 답안
# 걸린 시간: 92ms
# 값 초기화를 잘 해주거나 ~ 1 기반 인덱스를 사용하거나 ~
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
ground = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = ground[0][0] # 값 초기화 잘 체크하기

for i in range(N):
  for j in range(M):
    if 0 < i < N and 0 < j < M: dp[i][j] = max(dp[i-1][j] + ground[i][j], dp[i][j-1] + ground[i][j])
    elif 0 < i < N: dp[i][j] = dp[i-1][j] + ground[i][j] # 1행
    elif 0 < j < M: dp[i][j] = dp[i][j-1] + ground[i][j] # 1열

print(dp[N-1][M-1])