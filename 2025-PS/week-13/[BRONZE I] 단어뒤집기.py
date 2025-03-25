# https://www.acmicpc.net/problem/9093

# 내 답안
# 걸린 시간: 116ms
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
  words = input().strip().split()
  for word in words:
    print(word[::-1], end=' ')
  print()