# https://www.acmicpc.net/problem/1927

# 내 답안
# 걸린 시간: 228ms
# 우선순위 큐: 추가 - put(값) / 삭제 - get()
# 우선 순위 큐가 비어있는지 확인할 때는 que.empty()를 사용한다 (!)
from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
que = PriorityQueue()
for _ in range(N):
  value = int(input().strip())
  if value == 0:
    if not que.empty(): print(str(que.get()) + '\n')
    else: print('0\n')
  else: que.put(value)

# heapq를 사용한 답안
# 걸린 시간: 120ms
# heapq: 추가 - heapq.heappush(힙 리스트, 값) / 삭제 - heapq.heappop(힙 리스트)
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
heap = []
result = []

for _ in range(N):
  command = int(input().strip())
  if command == 0:
    if len(heap) == 0:
      result.append(0)
    else:
      result.append(heapq.heappop(heap))
  else:
    heapq.heappush(heap, command)

for i in result: print(i)