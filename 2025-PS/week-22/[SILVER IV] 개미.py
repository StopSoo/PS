# https://www.acmicpc.net/problem/3048

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 시뮬레이션
import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
G1 = input().strip()
G2 = input().strip()
T = int(input())

status = G1[::-1] + G2
for _ in range(T):
  i = 0
  while i < N1 + N2:
    if (i < N1 + N2 - 1) and (status[i] in G1 and status[i+1] in G2):
      status = status[:i] + status[i+1] + status[i] + status[i+2:]
      i += 2
    else: i += 1
print(status)