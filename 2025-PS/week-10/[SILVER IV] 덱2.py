# https://www.acmicpc.net/problem/28279

# 내 답안
# 걸린 시간: 1368ms
# deque 라이브러리 사용: 추가 - append(값), appendleft(값) / 삭제 - pop(), popleft()
from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
N = int(input().strip())
for _ in range(N):
  order = list(map(int, input().strip().split()))
  if order[0] == 1: deq.appendleft(order[1])
  elif order[0] == 2: deq.append(order[1])
  elif order[0] == 3: print(deq.popleft() if deq else -1)
  elif order[0] == 4: print(deq.pop() if deq else -1)
  elif order[0] == 5: print(len(deq))
  elif order[0] == 6: print(1 if not deq else 0)
  elif order[0] == 7: print(deq[0] if deq else -1)
  elif order[0] == 8: print(deq[-1] if deq else -1)