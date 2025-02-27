# https://www.acmicpc.net/problem/1904

# 내 답안
# 걸린 시간: 400ms
# 인덱스 에러 -> N이 1부터 시작되기 때문에 범위를 잘 체크할 것 (!)
# 길이가 3 -> 001, 100, 111
# 길이가 4 -> 0000, 0011, 1001, 1100, 1111
N = int(input())

dp = [0] * (N+1)
dp[1] = 1
if N >= 2: dp[2] = 2
if N >= 3:
  for i in range(3, N+1):
    dp[i] = ((dp[i-1] % 15746) + (dp[i-2] % 15746)) % 15746

print(dp[N])