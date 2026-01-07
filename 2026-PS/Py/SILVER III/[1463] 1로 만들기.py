# https://www.acmicpc.net/problem/1463
# 260107 풀이
# 알고리즘: DP
# 시간: 500ms
N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] += dp[i - 1] + 1 # 1을 빼는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])