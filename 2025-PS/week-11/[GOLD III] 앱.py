# https://www.acmicpc.net/problem/7579

# 답안
# 걸린 시간: 700ms
# 12865_평범한 배낭 문제를 참고해서 풀이.
# 보통 dp 테이블을 N번 물건까지 살펴보고 M바이트를 얻기 위한 최소 비용으로 구성.
# 하지만 M이 최대 1000만이므로, dp 테이블을 N과 최대 100인 비활성화 비용으로 구성하기 (!!!!)
# -> N번 물건까지 살펴보고 비용 C로 얻을 수 있는 최대 메모리
INF = int(1e12)
MAX = 10001

N, M = map(int, input().split())

mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[0] * (MAX) for _ in range(N+1)]

for n in range(1, N+1):
  for c in range(0, MAX):
    dp[n][c] = dp[n-1][c]
    if c - costs[n] >= 0:
      dp[n][c] = max(dp[n][c], dp[n-1][c-costs[n]] + mems[n])

ans = INF
for c in range(0, MAX):
  if dp[N][c] >= M: ans = min(ans, c)
print(ans)