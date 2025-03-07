# https://www.acmicpc.net/problem/24511

# 내 답안
# 걸린 시간: 200ms
# 처음에는 N, M이 최대 10만이길래 어떻게 풀지,,? 고민 한 10분 정도 했음
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
ds = list(map(int, input().strip().split()))
elements = list(map(int, input().strip().split()))
M = int(input())
push_elements = list(map(int, input().strip().split()))

deq = deque(elements[i] for i in range(len(ds)) if ds[i] == 0) # 큐인 것들만 담기
for element in push_elements:
  deq.appendleft(element)
  print(deq.pop(), end=' ')