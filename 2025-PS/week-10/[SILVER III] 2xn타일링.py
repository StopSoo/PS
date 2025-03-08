# https://www.acmicpc.net/problem/11726

# 내 답안
# 걸린 시간: 40ms
# DP라는 건 알았지만 규칙을 찾을 자신이 없었는데, 그냥 작은 수부터 해보다보니 풀림 ~
# 인덱스 에러를 조심하자 (!)
n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2
if n >= 3:
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])