# https://www.acmicpc.net/problem/16493

# 내 답안
# 걸린 시간: 1596ms
# DP 알고리즘 분류 타고 들어왔는데 브루트포스로 풀기 ...
# 처음에 런타임 에러 -> result가 빈 배열일 경우 0 에러 처리 해줘야 함 (!)
from itertools import combinations

N, M = map(int, input().split())
result = []
chapters = list(list(map(int, input().split())) for _ in range(M))

for i in range(M):
  for comb in combinations(range(M), i+1):
    if sum(chapters[ind][0] for ind in comb) <= N:
      result.append(sum(chapters[ind][1] for ind in comb))

print(max(result) if result else 0)

# DP(배낭 문제)로 풀기
N, M = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(M)]

dp = [0] * (N + 1)

for time, score in chapters:
  for i in range(N, time - 1, -1):
    dp[i] = max(dp[i], dp[i - time] + score)

print(max(dp))
