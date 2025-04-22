# https://www.acmicpc.net/problem/28066

# 내 답안
# 걸린 시간: 428ms
from collections import deque

N, K = map(int, input().split())
deq = deque(range(1, N+1))
while True:
  if len(deq) >= K:
    deq.rotate(-1) # 첫 번째 청설모는 냅두기
    for _ in range(K-1): deq.popleft()
  else:
    print(deq[0])
    break