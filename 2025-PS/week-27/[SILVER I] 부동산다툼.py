# https://www.acmicpc.net/problem/20364

# 내 답안 
# 걸린 시간: 1380ms
# 자료구조: 트리
import sys
input = sys.stdin.readline
from collections import defaultdict

N, Q = map(int, input().strip().split())
numbers = list(int(input().strip()) for _ in range(Q))
checked = [0] * (N + 1)

for number in numbers:
  path = []
  i = number
  while i >= 1: # 경로 수집
    path.append(i)
    i //= 2
  
  for p in path[::-1]:
    if checked[p]: # 가장 가까운 점유된 땅 출력
      print(p)
      break
  else: # 없으면 마지막 땅 점유 후 0 출력
    checked[path[0]] = 1
    print(0)