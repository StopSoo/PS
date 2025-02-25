# https://www.acmicpc.net/problem/11723

# 내 답안
# 걸린 시간: 3236ms
import sys
input = sys.stdin.readline

s = set()
M = int(input().strip())
for i in range(M):
  orders = input().strip().split()
  if orders[0] == "add" and int(orders[1]) not in s: 
    s.add(int(orders[1]))
  elif orders[0] == "remove" and int(orders[1]) in s: 
    s.remove(int(orders[1]))
  elif orders[0] == "check":
    print(1 if int(orders[1]) in s else 0)
  elif orders[0] == "toggle":
    if int(orders[1]) in s: s.remove(int(orders[1]))
    else: s.add(int(orders[1]))
  elif orders[0] == "all":
    s = set(range(1, 21))
  elif orders[0] == "empty": s = set()
