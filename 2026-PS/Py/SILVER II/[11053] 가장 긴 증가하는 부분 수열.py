# https://www.acmicpc.net/problem/11053
# 260121 풀이
# 알고리즘: LIS
# 시간: 96ms

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))