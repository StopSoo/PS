# https://www.acmicpc.net/problem/17219

# 내 답안
# 걸린 시간: 216ms
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
dt = {}
for _ in range(N):
  address, pw = input().strip().split()
  dt[address] = pw

for _ in range(M): print(dt[input().strip()])