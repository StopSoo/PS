# https://www.acmicpc.net/problem/1495

# 내 답안
# 걸린 시간: 48ms
# 나는 매 반복마다 볼륨 설정이 가능한지 체크했는데, 생각해보면 마지막에 빈 집합인지만 체크해도 가능 (!)
N, start_volumn, max_volumn = map(int, input().split())
volumns = list(map(int, input().split()))
dp = [set() for _ in range(N)]
for i in range(N):
  if i == 0:
    if start_volumn + volumns[i] <= max_volumn: dp[i].add(start_volumn + volumns[i])
    if start_volumn - volumns[i] >= 0: dp[i].add(start_volumn - volumns[i])
  else: 
    for v in dp[i-1]:
      if v + volumns[i] <= max_volumn: dp[i].add(v + volumns[i])
      if v - volumns[i] >= 0: dp[i].add(v - volumns[i])

if dp[N-1] == set(): print(-1)
else: print(max(dp[N-1]))