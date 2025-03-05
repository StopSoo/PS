# https://www.acmicpc.net/problem/11279

# 내 답안
# 걸린 시간: 276ms
from queue import PriorityQueue
import sys
input = sys.stdin.readline

que = PriorityQueue()
N = int(input().strip())
for _ in range(N):
  value = int(input().strip())
  if value == 0:
    if not que.empty(): print(que.get()[1])
    else: print(0)
  else:
    que.put((-value, value)) # -를 붙여서 값을 같이 넣기 (!)

# heapq를 활용한 답안
# 걸린 시간: 108ms
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
heap = []
for _ in range(N):
  value = int(input().strip())
  if value == 0:
    if heap: print(-heapq.heappop(heap)) # 값을 빼서 -를 붙여 출력하기
    else: print(0)
  else:
    heapq.heappush(heap, -value) # heappush할 때 값에 -를 붙여서 넣기