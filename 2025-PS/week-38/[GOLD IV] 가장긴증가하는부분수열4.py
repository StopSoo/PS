# https://www.acmicpc.net/problem/14002

# 내 답안
# 걸린 시간: 120ms
# 알고리즘: DP & 역추적
# 수열에 들어가는 값의 범위가 최대 1000이므로 O(N^2)인 DP를 이용.
N = int(input())
numbers = [0] + list(map(int, input().split()))
# dp 배열 구하기
dp = [-1] * (N + 1)
dp[1] = 1
for n in range(2, N+1):
  best = 0
  for i in range(1, n):
    if numbers[n] > numbers[i]:
      best = max(best, dp[i]) # dp[i]를 넣는 게 뽀인트(!)
  dp[n] = best + 1
# LIS 배열 구하기 (역추적)
len_lis = max(dp) # LIS의 길이
current_length = len_lis
lis = []
for i in range(N, 0, -1):
  # numbers[i] <= lis[-1]: 등호를 포함함으로써 여러 LIS 중 하나를 뽑아내게 됨.
  if dp[i] == current_length and (not lis or numbers[i] <= lis[-1]):
    lis.append(numbers[i])
    current_length -= 1

lis.reverse()

print(len_lis)
print(*lis)