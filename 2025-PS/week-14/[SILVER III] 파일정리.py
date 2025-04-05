# https://www.acmicpc.net/problem/20291

# 내 답안
# 걸린 시간: 184ms
# 빠른 입출력을 무조건 사용해야죠 !!! 
import sys
input = sys.stdin.readline

N = int(input().strip())
dt = dict()
for _ in range(N):
  name = input().strip().split('.')
  dt[name[1]] = dt.get(name[1], 0) + 1
for name, count in sorted(dt.items()):
  print(name, count)