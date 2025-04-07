# https://www.acmicpc.net/problem/4358

# 내 답안
# 걸린 시간: 496ms
# 파이썬에서의 EOF 입력 처리와 소수 포맷팅에 대하여 (!)
import sys
input = sys.stdin.readline

dt = dict()
total = 0
while True:
  name = input()
  
  if not name: break # EOF일 경우 ""가 들어옴 
  name = name.strip()
  if name:
    dt[name] = dt.get(name, 0) + 1
    total += 1

for name, count in sorted(dt.items()):
  print(f"{name} {count / total * 100:.4f}")