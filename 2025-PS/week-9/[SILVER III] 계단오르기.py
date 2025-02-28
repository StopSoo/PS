# https://www.acmicpc.net/problem/2579

# 내 답안
# 걸린 시간: 40ms (N이 300까지라 충분히 빠름)
# DP 배열에 들어갈 값은 다음과 같이 두 종류로 계산한다. (점화식)
# 1) 두 계단 전에서 오는 경우 -> dp[i-2] + scores[i]
# 2) 세 계단 전에서 오는 경우 -> dp[i-3] + scores[i-1] + scores[i]
N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

if N == 1:
  print(scores[1])
else:
  dp = [0] * (N+1) # i번째 계단까지 올라갔을 때 최대 점수

  dp[1] = scores[1]
  if N >= 2: dp[2] = scores[1] + scores[2]

  for i in range(3, N+1): # 점화식 사용
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
  print(dp[N])