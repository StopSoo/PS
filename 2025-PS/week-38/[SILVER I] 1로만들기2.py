# https://www.acmicpc.net/problem/12852

# 답안
# 걸린 시간: 576ms
# 알고리즘: DP & 역추적
N = int(input())
dp = [0] * (N + 1)
prev = [0] * (N + 1) # 역추적을 위함

for i in range(2, N + 1):
  dp[i] = dp[i - 1] + 1
  prev[i] = i - 1

  # 2로 나누어 떨어지고 갱신 필요가 있을 때
  if i % 2 == 0 and dp[i] > dp[i // 2] + 1: 
    dp[i] = dp[i // 2] + 1
    prev[i] = i // 2
  # 3으로 나누어 떨어지고 갱신 필요가 있을 때
  if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
    dp[i] = dp[i // 3] + 1
    prev[i] = i // 3

print(dp[N])

# 경로 역추적
path = []
cur = N
while cur != 0:
  path.append(cur)
  if cur == 1:
    break
  cur = prev[cur]
print(*path)