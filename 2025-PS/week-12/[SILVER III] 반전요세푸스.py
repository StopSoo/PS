# https://www.acmicpc.net/problem/20301

# 내 답안
# 걸린 시간: 64ms
from collections import deque

N, K, M = map(int, input().split())
deq = deque(range(1, N+1))

count = 0 # 제거한 사람의 수
is_reversed = False 
answer = []
while deq:
  if not is_reversed:
    deq.rotate(-(K-1))
    answer.append(deq.popleft())
    count += 1
  else:
    deq.rotate(K)
    answer.append(deq.popleft())
    count += 1
  if count == M:
    is_reversed = not is_reversed
    count = 0
  
print(*answer, sep='\n')