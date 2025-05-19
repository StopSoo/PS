# https://www.acmicpc.net/problem/1966

# 첫 번째 답안: 큐 이용하기
# 걸린 시간: 60ms
# 큐에 값을 넣을 때 인덱스와 함께 넣는 것이 가장 효율적!
import sys
input = sys.stdin.readline
from collections import deque

def print_order(N, M, importance):
  queue = deque([(i, p) for i, p in enumerate(importance)])
  order = 0

  while queue:
    cur = queue.popleft()
    if any(cur[1] < q for _, q in queue): queue.append(cur)
    else:
      order += 1
      if cur[0] == M: return order

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  importance = list(map(int, input().split()))
  print(print_order(N, M, importance))

# 두 번째 답안: 시뮬레이션 -> 문제의 조건을 코드로 직접 구현 (큐 없이)
# 걸린 시간: 40ms
import sys
input = sys.stdin.readline

def print_order(N, M, importance):
  queue = [(i, p) for i, p in enumerate(importance)]
  order = 0

  while queue:
    cur = queue.pop(0)
    if any(cur[1] < q[1] for q in queue): queue.append(cur)
    else:
      order += 1
      if cur[0] == M: return order

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  importance = list(map(int, input().split()))
  print(print_order(N, M, importance))