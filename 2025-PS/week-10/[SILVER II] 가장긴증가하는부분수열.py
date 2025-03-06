# https://www.acmicpc.net/problem/11053

# 내 답안
# 걸린 시간: 116ms
# LIS: 가장 큰 증가하는 부분 수열 
# dp[n] = n번쨰 원소까지 살펴봤을 때의 LIS
# Bottom-Up 방식 (!)
N = int(input())
numbers = [0] + list(map(int, input().split())) # 인덱스 1부터 시작
dp = [-1] * (len(numbers)+1) # 인덱스 1부터 시작

dp[1] = 1 # 첫 번째 원소의 LIS는 1

for n in range(2, N+1): # dp[n]
  best = 0
  for i in range(1, n):
    if numbers[n] > numbers[i]: # 갱신이 가능한 경우만 체크 
      best = max(best, dp[i])
  dp[n] = best + 1

print(max(dp[1:]))

# 다른 사람의 답안
# 이게 더 이해가 잘 되는 듯 ...!
n = int(input())
arr = list(map(int,input().split()))
dp=[1] * n # 기본값이 모두 1

for i in range(1, n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))