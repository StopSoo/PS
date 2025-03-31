# https://www.acmicpc.net/problem/5635

# 내 답안
# 걸린 시간: 32ms
import sys
input = sys.stdin.readline

N = int(input().strip())
dt = dict()
for i in range(N):
  name, d, m, y = input().strip().split()
  dt[name] = [int(y), int(m), int(d)]

sorted_dt = sorted(dt.values(), key=lambda x: [x[0], x[1], x[2]])
max_p, min_p = "", ""
for p in dt:
  if dt[p] == sorted_dt[0]: max_p = p
  if dt[p] == sorted_dt[-1]: min_p = p
print(min_p)
print(max_p)

# 이차원 배열을 활용해서 나름 더 간단하게 한다면?
N = int(input())
li = []
for _ in range(N):
  name, d, m, y = map(str, input().split())
  d = int(d); m = int(m); y=int(y)
  li.append([name,(y,m,d)])
    
li.sort(key=lambda x: (x[1][0], x[1][1], x[1][2]))

print(li[-1][0])
print(li[0][0])