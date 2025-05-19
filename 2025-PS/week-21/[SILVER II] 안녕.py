# https://www.acmicpc.net/problem/1535

# 내 답안
# 걸린 시간: 40ms
# 알고리즘: 배낭 문제
# DP 배열 갱신할 때 100부터 h까지로 범위 잡는 게 헷갈렸음.
import sys
input = sys.stdin.readline

N = int(input())
health = list(map(int, input().strip().split()))
joy = list(map(int, input().strip().split()))

dp = [0] * 101
for h, j in zip(health, joy):
  for i in range(100, h - 1, -1):
    if i - h > 0: # 살아있는 상태일 때만 체크 후 갱신
      dp[i] = max(dp[i], dp[i - h] + j)
print(max(dp))