# https://www.acmicpc.net/problem/2161

# 내 답안
# 걸린 시간: 60ms
from collections import deque

N = int(input())
deq = deque(range(1, N+1))

answer = []
while deq:
  answer.append(deq.popleft())
  deq.rotate(-1)
print(*answer)