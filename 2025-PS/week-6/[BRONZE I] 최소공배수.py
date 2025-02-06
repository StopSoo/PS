# https://www.acmicpc.net/problem/1934

# 내 답안
from math import lcm
T = int(input())
for _ in range(T):
  num1, num2 = map(int, input().split())
  print(lcm(num1, num2))