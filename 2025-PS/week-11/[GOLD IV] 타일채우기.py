# https://www.acmicpc.net/problem/2133

# 답안
# 걸린 시간: 36ms
# 점화식을 찾는 것이 중요한데, 점화식 찾기가 힘들었음 !!
# 1) 어떻게 끝나는지를 먼저 생각해보고
# 2) 예외 경우가 있는지 체크해볼 것
# dp[n] = 3*dp[n-2] + 2*(dp[n-4] + dp[n-6] + dp[n-8] + ...)
N = int(input())
dp = [0] * (N + 2) 
dp[2] = 3
# dp[3] = 0
# dp[4] = 11 # dp[2] * 3 + 2(특수) = 11
# dp[5] = 0
# dp[6] = 41 # dp[4] * 3 + 2 * dp[2] + 2(특수) = 41
# dp[7] = 0
# dp[8] = 153 # dp[6] * 3 + 2 * dp[4] + 2 * dp[2] + 2(특수) = 123 + 22 + 6 + 2

for i in range(4, N+1):
  if i % 2 == 0: # 짝수일 경우 값 갱신
    dp[i] += dp[i-2] * 3
    for j in range(i-4, -1, -2):
      dp[i] += 2 * dp[j]
    dp[i] += 2 # 특수 케이스

print(dp[N])