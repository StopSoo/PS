# https://www.acmicpc.net/problem/8394

# 내 답안
# 걸린 시간: 2136ms
# 마지막 사람이 혼자 있다면, 나머지 n-1명은 dp[n-1]가지 방법으로 악수할 수 있음.
# 마지막 사람이 바로 앞 사람과 악수한다면, 그 둘을 묶고 나머지 n-2명은 dp[n-2]가지 방법으로 악수할 수 있음.
# 고전적인 피보나치 점화식 문제 (!)
N = int(input())
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
  dp[i] = (dp[i-1] + dp[i-2]) % 10
print(dp[N])