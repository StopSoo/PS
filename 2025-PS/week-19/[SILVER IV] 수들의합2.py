# https://www.acmicpc.net/problem/2003

# 내 답안
# 걸린 시간: 44ms
# 알고리즘: 누적합 / 투포인터
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split())) # 1 기반 인덱스
for i in range(1, N+1):
  numbers[i] += numbers[i-1] # 누적 합

i, j = 0, 1
count = 0 # 경우의 수
while True:
  if j == N + 1: break # 종료 조건
  if numbers[j] - numbers[i] == M:
    count += 1
    j += 1
  elif numbers[j] - numbers[i] > M: i += 1
  else: j += 1

print(count)