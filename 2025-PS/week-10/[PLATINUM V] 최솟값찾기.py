# https://www.acmicpc.net/problem/11003

# 내 답안
# 걸린 시간: 7132ms -> write 추가해서 6000ms
# 튜플이 리스트보다 효율적이다.
import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, L = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
mydeq = deque()

for i in range(N):
  while mydeq and mydeq[-1][0] > numbers[i]:
    mydeq.pop()
  mydeq.append((numbers[i], i))
  if mydeq[0][1] <= i-L: # 윈도우 범위를 벗어나면
    mydeq.popleft()
  print(str(mydeq[0][0]) + ' ')