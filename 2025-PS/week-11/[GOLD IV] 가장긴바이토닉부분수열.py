# https://www.acmicpc.net/problem/11054

# 답안
# 걸린 시간: 220ms
# 11053_가장긴증가하는부분수열 문제를 참고하면 됨 (!) 하지만 제대로 이해하진 못함 ...
N = int(input())
numbers = list(map(int, input().split()))
dp1 = [0] * N
dp2 = [0] * N
dp1[0] = dp2[N-1] = 1
# dp1
for n in range(1, N):
  dp1[n] = 1
  for i in range(0, n): 
    if numbers[i] < numbers[n]:
      dp1[n] = max(dp1[n], dp1[i]+1)
# dp2
for n in range(N-2, -1, -1):
  dp2[n] = 1
  for i in range(N-1, n, -1):
    if numbers[i] < numbers[n]:
      dp2[n] = max(dp2[n], dp2[i]+1)

ans = 0
for n in range(N):
  ans = max(ans, dp1[n] + dp2[n] - 1)
print(ans)
