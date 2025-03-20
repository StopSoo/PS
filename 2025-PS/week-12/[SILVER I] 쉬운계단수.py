# https://www.acmicpc.net/problem/10844

# 내 답안
# 걸린 시간: 40ms
# 결과값들 간에 규칙 찾으려다 실패하고 ...
# DP라는 카테고리를 이용해 생각해보면 2차원 배열로 구현할 수 있다는 것 (!)
N = int(input())
dp = [[0] + [1]*9]
for i in range(1, N): 
  dp.append([])
  for j in range(0, 10):
    if j-1 >= 0:
      if j+1 < 10:
        dp[i].append(dp[i-1][j-1] + dp[i-1][j+1])
      else: # j == 9
        dp[i].append(dp[i-1][j-1])
    else: # j == 0
      dp[i].append(dp[i-1][j+1])

print(sum(dp[N-1]) % 1000000000)