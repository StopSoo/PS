# https://www.acmicpc.net/problem/11660

# 내 답안
# 걸린 시간: 1272ms
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = [[0 for _ in range(N+1)] for _ in range(N+1)] # 1열, 1행에 0으로 두르도록 설정
for i in range(1, N+1):
  row = [0] + list(map(int, input().strip().split()))
  for j in range(1, N+1):
    numbers[i][j] = row[j]
sums = numbers[:]

for i in range(1, N+1): # 누적 합 (!)
  for j in range(1, N+1):
    if i == 1 and j == 1: continue
    elif i == 1:
      sums[i][j] = sums[i][j-1] + numbers[i][j]
    elif j == 1:
      sums[i][j] = sums[i-1][j] + numbers[i][j]
    else:
      sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + numbers[i][j] 

for _ in range(M): # 2차원 배열 구간 합 구하기 (!)
  x1, y1, x2, y2 = map(int, input().strip().split())
  print(sums[x2][y2] - (sums[x1-1][y2] + sums[x2][y1-1] - sums[x1-1][y1-1]))