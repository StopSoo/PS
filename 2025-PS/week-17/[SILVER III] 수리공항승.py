# https://www.acmicpc.net/problem/1449

# 내 답안
# 걸린 시간: 40ms
import sys
input = sys.stdin.readline

N, L = map(int, input().strip().split())
pos = sorted(map(int, input().strip().split()))

count = 0
s = -1
for i in range(N):
  if s == -1 or pos[i] - s + 1 > L: 
    s = pos[i]
    count += 1
print(count)