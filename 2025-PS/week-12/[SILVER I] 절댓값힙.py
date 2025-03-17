# https://www.acmicpc.net/problem/11286

# 내 답안
# 걸린 시간: 128ms
# PriorityQueue()에는 empty()라는 함수가 있다 (!)
# 하지만 여러 가지 조건을 따져봤을 때 이 문제는 heapq를 사용해야 하는 문제이다 (!)
import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = [] # 우선순위 큐

for _ in range(N):
  value = int(input())
  if value != 0:
    heapq.heappush(hq, (abs(value), value)) # 절댓값을 기준으로 동작.
  else:
    if not hq: # 빈 배열이라면
      print(0)
    else:
      print(heapq.heappop(hq)[1])