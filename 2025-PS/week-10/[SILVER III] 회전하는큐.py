# https://www.acmicpc.net/problem/1021

# 내 답안
# 걸린 시간: 60ms
# 문제 이해하는 데 10분은 걸린 듯 ;; 푸는 데는 50분?
# 큐 값이 중요한 게 아니라, 그 값의 큐 내 인덱스가 더 중요하다는 것을 (!)
from collections import deque

N, M = map(int, input().split())
deq = deque(range(1, N+1))
targets = list(map(int, input().split()))
count = 0

for target in targets:
  if deq[0] == target: deq.popleft() # 덱 맨 앞 원소와 같다면 pop만 하기
  else: # 더 가까운 쪽으로 돌려야 함
    if deq.index(target) > len(deq)//2: 
      count += abs(len(deq) - deq.index(target))
      deq.rotate(len(deq) - deq.index(target)) 
      deq.popleft()
    else: 
      count += deq.index(target)
      deq.rotate(-(deq.index(target))) # 왼쪽으로 돌려서 맨 앞에 위치시키기
      deq.popleft()
print(count)
