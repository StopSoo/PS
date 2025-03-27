# https://www.acmicpc.net/problem/15652

# 내 답안
# 걸린 시간: 52ms
# 백트래킹을 이용한 답안
N, M = map(int, input().split())
ans = []

def back():
  if len(ans) == M:
    print(*ans)
    return
  for i in range(1, N+1): # 중복 허용
    if (not ans) or (ans and i >= ans[-1]): # 비내림차순
      ans.append(i)
      back()
      ans.pop()

back()

# 중복 조합(combinations_with_replacement) 이용하기 (!)
# 걸린 시간: 52ms
import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement as comb

N, M = map(int, input().split())
for c in comb(range(1, N+1), M):
  print(*c)