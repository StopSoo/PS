# https://www.acmicpc.net/problem/1758

# 내 답안
# 걸린 시간: 88ms
import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)], reverse=True)

tips = 0
for i in range(N):
  value = numbers[i] - i
  if value < 0: continue
  tips += value
print(tips)