# https://www.acmicpc.net/problem/14916

# 내 답안
# 걸린 시간: 88ms
n = int(input())
dp = [0] * 100001
dp[1] = -1 # 2원과 5원으로 거스름돈을 줄 수 없음
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1
for i in range(6, n+1):
  if dp[i-2] != -1 and dp[i-5] != -1:
    dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)
  elif dp[i-2] != -1:
    dp[i] = dp[i-2] + 1
  elif dp[i-5] != -1:
    dp[i] = dp[i-5] + 1
  else:
    dp[i] = -1

print(dp[n])

# 다른 사람의 답안
# 걸린 시간: 40ms
n = int(input())

if n == 1 or n == 3:
  print(-1)
else:
  if n % 5 == 0:
    print(n // 5)
  elif n % 5 == 2:
    print(n // 5 + 1)
  elif n % 5 == 1 or n % 5 == 4:
    print(n // 5 + 2)
  else:
    print(n // 5 + 3)