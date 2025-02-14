# https://www.acmicpc.net/problem/2577

# 내 답안
from math import prod
result = str(prod([int(input()) for _ in range(3)]))
# checks = [0] * 10
# for r in result: checks[int(r)] += 1
checks = [result.count(str(num)) for num in range(0, 10)]
for c in checks: print(c)