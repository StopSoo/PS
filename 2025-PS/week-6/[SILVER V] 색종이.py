# https://www.acmicpc.net/problem/2563

# 내 답안
import sys
input = sys.stdin.readline
# print = sys.stdout.write

check = [[0]*100 for _ in range(100)]
T = int(input())
for _ in range(T):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      check[i][j] = 1
print(sum([check[i].count(1) for i in range(100)]))