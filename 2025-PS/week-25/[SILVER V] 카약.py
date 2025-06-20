# https://www.acmicpc.net/problem/2890

# 내 답안
# 걸린 시간: 32ms
import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
point_count = [float('inf')] * (R + 1)
rank = [0] * (R + 1)  
for i in range(R):
  line = input().strip()
  l = line[1:C-1].split('.')
  flag = False
  count = 0
  if not all(x == '' for x in l):
    for ch in l:
      if ch.isdigit(): 
        idx = int(ch[0])
        flag = True
      else:
        if flag: count += 1
    point_count[idx] = count   

sorted_count = sorted(set(point_count))
for i in range(1, 10):
  if point_count[i] != float('inf'):
    rank[i] = sorted_count.index(point_count[i]) + 1

for i in range(1, 10):
  if point_count[i] != float('inf'):
    print(rank[i])
