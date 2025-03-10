# https://www.acmicpc.net/problem/1912

# 내 답안 + 보완
# 걸린 시간: 92ms
# 누적합을 구해놓고 해야 하는 줄 알았는데 안해도 되는 거였음 !!
# Bottom-Up 방식
import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().strip().split()))

dp = [0 for _ in range(n)]
dp[0] = numbers[0]
for i in range(1, n):  
  dp[i] = max(0, dp[i-1]) + numbers[i] # 누적합이 음수이면 끊는 게 낫고, 양수이면 누적합하는 게 나음 (!)

print(max(dp))