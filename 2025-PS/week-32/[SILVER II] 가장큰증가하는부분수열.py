# https://www.acmicpc.net/problem/11055

# 내 답안
# 걸린 시간: 144ms
# 알고리즘: DP
# 중간에 막혀서 도움 받아서 완성했는데, 복잡하게 생각할 거 없다 ...
N = int(input())
numbers = list(map(int, input().split()))
dp = numbers[:] # dp[i] = i를 마지막으로 하는 증가 부분 수열의 최대 합

for i in range(N):
  for j in range(i):
    if numbers[i] > numbers[j]:
      dp[i] = max(dp[i], numbers[i] + dp[j])

print(max(dp))