# https://www.acmicpc.net/problem/11057

# 내 답안
# 걸린 시간: 44ms
# 10844_쉬운 계단수를 참고해서 풀음 !! 꽤나 오래 고민함. 비슷한 듯 다름 !!
N = int(input())
dp = [[0]*10, [1]*10]
for i in range(2, N+1): 
  dp.append([])
  for j in range(10):
    if j-1 >= 0:
      dp[i].append(dp[i-1][j] + dp[i][j-1])
    else: # j == 0
      dp[i].append(dp[i-1][j])

print(sum(dp[N]) % 10007)

# 다른 답안
N = int(input())
dp = [1]*10

for _ in range(N-1):
  for j in range(10):
    dp[j] = sum(dp[j:])

print(sum(dp) % 10007)