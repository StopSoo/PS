# https://www.acmicpc.net/problem/1535

# 내 답안
# 걸린 시간: 40ms
# DP / 배낭 문제 -> 16493번 문제의 배낭문제 코드 참고해서 풀이.
N = int(input())
health = list(map(int, input().split()))
joy = list(map(int, input().split()))

sejoon = [[h, j] for h, j in zip(health, joy)]
dp = [0] * 101 # 기쁨의 양을 저장
for h, j in sejoon:
  for i in range(100, h - 1, -1):
    if i-h > 0: # 체력이 0 초과일 때만
      dp[i] = max(dp[i], dp[i-h] + j)

print(max(dp))