# https://www.acmicpc.net/problem/1002

# 내 답안
# 걸린 시간: 32ms
# 알고리즘: 수학/기하학
# 첫 코드에서 놓쳤던 부분 -> 내접
import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())

  dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # 두 원의 중심 사이 거리
  if x1 == x2 and y1 == y2 and r1 == r2: # 완전히 일치하는 경우
    print(-1)
  elif (dist > r1 + r2) or (dist < abs(r1 - r2)): # 두 원이 접점이 없음
    print(0)
  elif (dist == r1 + r2) or (dist == abs(r1 - r2)): # 두 원이 접함(외접 & 내접)
    print(1)
  elif r1 - r2 < dist < r1 + r2: # 두 원이 두 점에서 만남
    print(2)