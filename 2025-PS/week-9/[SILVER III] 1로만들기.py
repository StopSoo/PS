# https://www.acmicpc.net/problem/1463

# 내 답안
# 걸린 시간: 460ms
# 처음에 작성했던 코드는 재귀 깊이가 너무 커져서 런타임 에러 발생.
# DP는 Bottom-Up 방식으로 작성하는 게 좋다 (!)

# def makeOne(n, dp):
#   # base case 
#   if n == 1: return 0
#   if dp[n] != -1: return dp[n]

#   result = makeOne(n - 1, dp) + 1
#   if n % 2 == 0:
#     result = min(result, makeOne(n // 2, dp) + 1)
#   if n % 3 == 0:
#     result = min(result, makeOne(n // 3, dp) + 1)
  
#   dp[n] = result
#   return dp[n]

N = int(input())
dp = [0] * (N+1) # check list

for i in range(2, N+1):
  dp[i] = dp[i-1] + 1

  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
