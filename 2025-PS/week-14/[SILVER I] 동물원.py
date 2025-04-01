# https://www.acmicpc.net/problem/1309

# 답안
# 걸린 시간: 68ms
# 왜 난 점화식을 찾는 데 약할까 !?
# 점화식 이해하기: https://www.acmicpc.net/board/view/141421
N = int(input())
dp = [0] * (N+1)
dp[0] = 1 # N=0이라면 1가지
dp[1] = 3 # N=1이라면 3가지(X, 왼, 오)
if N >= 2:
  for i in range(2, N+1):
    dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901

print(dp[N])