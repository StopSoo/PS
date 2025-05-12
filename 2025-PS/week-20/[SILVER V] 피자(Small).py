# https://www.acmicpc.net/problem/14606

# 내 답안
# 걸린 시간: 36ms
# DP로 푸는 문제인데 풀다 보니 이렇게 풀게 됨. -> 최대 즐거움을 위해서는 항상 1씩 잘라가는 식으로 쪼개는 게 가장 유리하기 때문.
N = int(input())
if N == 1: print(0)
else: print(sum(range(1, N)))

# 의도된 풀이로 푼 코드
# 걸린 시간: 36ms
# 높이 n을 i와 n-i로 분리한다고 가정했을 때, 
# 두 탑을 쪼개기 전까지 각각 최대 즐거움을 dp[i], dp[n-i]만큼 느끼고
# 쪼개는 과정에서 i * (n-i)만큼의 즐거움을 추가로 느끼는 것.
N = int(input())

dp = [0] * (N + 1)
for n in range(2, N + 1):
  for i in range(1, n):
    dp[n] = max(dp[n], dp[i] + dp[n - i] + i * (n - i))

print(dp[N])
