# https://www.acmicpc.net/problem/15650

# 내 답안
# 걸린 시간: 36ms
from itertools import combinations

N, M = map(int, input().split())
for comb in combinations(range(1, N+1), M):
  print(*comb)

# 백트래킹으로 구현한 코드
# 걸린 시간: 40ms
N, M = map(int, input().split())
ans = []

def back():
  if len(ans) == M:
    print(" ".join(map(str, ans)))
    return
  for i in range(1, N+1):
    if i not in ans:
      if (not ans) or (ans and i > ans[-1]) :
        ans.append(i)
        back()
        ans.pop()

back()