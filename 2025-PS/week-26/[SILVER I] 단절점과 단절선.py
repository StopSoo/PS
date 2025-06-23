# https://www.acmicpc.net/problem/14675

# 내 답안
# 걸린 시간: 236ms
# 살짝 힌트 참고해서 풀이함. 근데 그냥 양방향 그래프로 풀어도 될 것 같음.
import sys
input = sys.stdin.readline
from collections import defaultdict

tin = [0] * 100001 # 해당 정점으로 들어오는 정점의 수
tout = [0] * 100001 # 해당 정점에서 뻗어나가는 정점의 수

N = int(input())
for _ in range(N-1):
  a, b = map(int, input().split())
  tin[a] += 1
  tout[a] += 1
  tin[b] += 1
  tout[b] += 1

q = int(input())
for _ in range(q):
  t, k = map(int, input().split())
  if t == 2: print("yes")
  else:
    if tin[k] == 1 and tout[k] == 1: print("no")
    else: print("yes")