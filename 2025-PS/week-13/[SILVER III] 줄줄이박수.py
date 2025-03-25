# https://www.acmicpc.net/problem/29718

# 내 답안
# 걸린 시간: 2052ms
# 두 번째 for문에서 계속 sum을 사용하는 것보다는, 한 번 더 가로로 누적하하고 슬라이딩 윈도우를 사용하는 것이 시간 복잡도 측면에서는 좋을 듯 !!
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
people = [list(map(int, input().strip().split())) for _ in range(N)]
A = int(input())
# 누적합
for i in range(M):
  for j in range(1, N):
    people[j][i] += people[j-1][i]

max_value = 0
for i in range(M-A+1):
  if sum(people[N-1][i:i+A]) > max_value:
    max_value = sum(people[N-1][i:i+A])
print(max_value)