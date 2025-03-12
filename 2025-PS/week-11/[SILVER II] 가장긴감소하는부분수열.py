# https://www.acmicpc.net/problem/11722

# 내 답안
# 걸린 시간: 132ms
# 11053_가장긴증가하는부분수열 문제를 참고하면 됨 (!) 하지만 제대로 이해하진 못함 ...
N = int(input())
numbers = list(map(int, input().split()))
dp = [1] * N # 기본값이 모두 1

for i in range(1, N): # 끝나는 인덱스
  for j in range(i):
    if numbers[i] < numbers[j]:
      dp[i] = max(dp[i], dp[j]+1)
print(max(dp))