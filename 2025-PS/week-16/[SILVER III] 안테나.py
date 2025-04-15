# https://www.acmicpc.net/problem/18310

# 내 답안
# 걸린 시간:
# IndexError: N==1일 때를 고려하지 않았기 때문.
import sys
input = sys.stdin.readline

N = int(input())
house = sorted(list(map(int, input().strip().split())))
answer = 0 # 안테나의 위치
min_dist = float('inf') # 집들 간의 거리의 합
if N == 1: print(house[0])
else:
  if N % 2 == 0:
    for i in [N//2-1, N//2]:
      dist = 0
      for j in range(N):
        if i == j: continue
        dist += abs(house[j] - house[i])
      if dist < min_dist:
        min_dist = dist
        answer = house[i]
  else:
    for i in [N//2-1, N//2, N//2+1]:
      dist = 0
      for j in range(N):
        if i == j: continue
        dist += abs(house[j] - house[i])
      if dist < min_dist:
        min_dist = dist
        answer = house[i]
  print(answer)

# 중앙값만 체크하면 된다는 논리를 반영한 코드
import sys
input = sys.stdin.readline

N = int(input())
house = sorted(list(map(int, input().strip().split())))

# 중앙값 출력
# N이 홀수든 짝수든, 항상 앞쪽 중앙값을 출력하면 된다.
print(house[(N - 1) // 2])