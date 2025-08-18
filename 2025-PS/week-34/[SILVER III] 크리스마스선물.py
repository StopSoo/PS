# https://www.acmicpc.net/problem/14235

# 내 답안
# 걸린 시간: 128ms
import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
  add = input().strip()
  if add == '0':
    if hq: print(-heapq.heappop(hq))
    else: print(-1)
  else:
    add = list(map(int, add.split()))
    for present in add[1:]:
      heapq.heappush(hq, -present)