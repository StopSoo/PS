# https://www.acmicpc.net/problem/11000

# 내 답안
# 걸린 시간: 308ms
import sys, heapq 
input = sys.stdin.readline

N = int(input())
q = []
times = []
for _ in range(N):
  s, t = map(int, input().split())
  times.append((s, t))
times.sort() # 시간들을 시작 시간 순으로 정렬해야 함(!)

for s, t in times:
  if not q or q[0] > s:
    heapq.heappush(q, t)
  elif q[0] <= s:
    heapq.heappop(q)
    heapq.heappush(q, t)

print(len(q))
