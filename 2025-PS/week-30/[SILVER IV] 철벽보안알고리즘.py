# https://www.acmicpc.net/problem/9322

# 내 답안
# 걸린 시간: 1984ms
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  one = input().strip().split()
  two = input().strip().split()
  order = {ind1: ind2 for ind1 in range(n) for ind2 in range(n) if one[ind1] == two[ind2]}
  pw = input().strip().split()

  answer = []
  for i in range(n):
    answer.append(pw[order[i]])
  print(' '.join(answer))