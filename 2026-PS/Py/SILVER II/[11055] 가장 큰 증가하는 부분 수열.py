# https://www.acmicpc.net/problem/11055
# 260122 풀이
# 알고리즘: DP
# 시간: 132ms

N = int(input())
A = list(map(int, input().split()))
dp = A[:] # dp[n] = n번째 원소를 마지막으로 하는 증가 부분 수열의 최대 합

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], A[i] + dp[j])

print(max(dp))