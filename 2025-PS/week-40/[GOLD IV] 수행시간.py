# https://www.acmicpc.net/problem/16169

# 답안
# 걸린 시간: 풀다가 막힘. 도움 받음.
# 알고리즘: 위상정렬 + DP

# 딕셔너리의 사이즈가 바뀐다는 오류
# 해결법 1) 순회할 때 딕셔너리 키 목록을 고정시켜 놓고 순회하기
# 해결법 2) in으로 존재 여부 확인 후 접근하기
from collections import defaultdict

n = int(input())
level = [0] * (n + 1)
speed = [0] * (n + 1) # 컴퓨터 작동 시간

dt = defaultdict(list)
for i in range(1, n + 1):
  c, t = map(int, input().split())
  level[i] = c
  speed[i] = t
  dt[c].append(i)
# dp[i] = i번 컴퓨터가 끝나는 시간
dp = [0] * (n + 1)
min_level = min(level[1:])
max_level = max(level[1:])

for c in range(min_level, max_level + 1):
  for i in dt[c]:
    if c == 1:
      dp[i] = speed[i]
    else:
      best = 0
      for j in dt[c-1]: # 이전 계급의 모든 컴퓨터
        best = max(best, dp[j] + (i - j) ** 2)
      dp[i] = best + speed[i]

print(max(dp))