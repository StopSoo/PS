# https://www.acmicpc.net/problem/11053

# 내 답안
# 알고리즘: DP
# 완전 틀린 풀이 -> 현재 인덱스 전의 모든 작은 값들을 고려하지 않고, max_index만 고려함. 
N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N
max_index = 0
for i in range(1, N):
  if numbers[max_index] < numbers[i]:
    dp[i] = dp[max_index] + 1
    max_index = i # 갱신

print(max(dp))

# 정답 코드
# 걸린 시간: 124ms
N = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[1] = 1
for n in range(2, N+1):
  best = 0
  for i in range(1, n):
    if numbers[n] > numbers[i]:
      best = max(best, dp[i]) # dp[i]를 넣는 게 뽀인트(!)
  dp[n] = best + 1

print(max(dp[1:]))