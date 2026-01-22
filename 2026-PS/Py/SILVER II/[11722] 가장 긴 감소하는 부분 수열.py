# https://www.acmicpc.net/problem/11722
# 260122 풀이
# 알고리즘: DP
# 시간: 128ms

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N # dp[n] = n번째 원소를 마지막으로 하는 감소 부분 수열의 길이

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))