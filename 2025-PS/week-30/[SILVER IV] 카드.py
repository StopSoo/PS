# https://www.acmicpc.net/problem/11652

# 내 답안
# 걸린 시간: 156ms
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
numbers = defaultdict(int)
for _ in range(N):
  num = int(input())
  numbers[num] += 1
sorted_numbers = sorted(numbers.keys(), key=lambda x: [-numbers[x], x])
print(sorted_numbers[0])