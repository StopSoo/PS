# https://www.acmicpc.net/problem/14494

# 내 답안
# 걸린 시간:
# 행열 구분을 잘하시길!
# 틀렸던 부분: 애초에 초기값 설정할 때 1, 2, 3, 4 ... 이렇게 늘어나게 했는데, 그 부분은 잘못 생각했었음!
n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1

for x in range(1, n+1):
  for y in range(1, m+1):
    if x == 1 and y == 1: continue  
    dp[x][y] = (dp[x-1][y] + dp[x][y-1] + dp[x-1][y-1]) % 1000000007

print(dp[n][m])