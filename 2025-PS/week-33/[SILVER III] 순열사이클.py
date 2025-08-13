# https://www.acmicpc.net/problem/10451

# 내 답안
# 걸린 시간: 440ms
# 알고리즘: 그래프 탐색
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node):
  global checked, dt

  checked[node] = 1
  if not checked[dt[node]]:
    dfs(dt[node])

T = int(input())
for _ in range(T):
  N = int(input())
  dt = defaultdict(int)
  numbers = [0] + list(map(int, input().split()))
  for i in range(1, N + 1):
    dt[i] = numbers[i]
  
  checked = [0] * (N + 1)
  cycle = 0
  for i in range(1, N + 1):
    if not checked[i]:
      dfs(i)
      cycle += 1
  
  print(cycle)