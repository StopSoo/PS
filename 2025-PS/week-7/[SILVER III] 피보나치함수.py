# https://www.acmicpc.net/problem/1003

# 내 답안
T = int(input())
# memoization
counts = [[1, 0], [0, 1], [1, 1]]
for i in range(3, 41):
  counts.append([counts[i-1][0] + counts[i-2][0], counts[i-1][1] + counts[i-2][1]])

for _ in range(T):
  ind = int(input())
  print(counts[ind][0], counts[ind][1])