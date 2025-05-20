# https://www.acmicpc.net/problem/1244

# 내 답안
# 걸린 시간: 32ms
# 알고리즘: 시뮬레이션
# 인덱스 에러에 조심하자, 항상 범위 체크를 하자 (!)
import sys
input = sys.stdin.readline

N = int(input())
switch = [-1] + list(map(int, input().split())) # 1기반 인덱스
students = int(input())
for _ in range(students):
  sex, num = map(int, input().split())
  if sex == 1: # 남학생이라면
    for i in range(1, N+1):
      if i % num == 0: switch[i] = (switch[i] + 1) % 2
  else: # 여학생이라면
    gap = 1
    while (num-gap >= 1) and (num+gap <= N): # 인덱스 에러 발생 주의 !!
      if switch[num-gap] == switch[num+gap]: gap += 1
      else: break
    for i in range(gap):
      if i == 0: switch[num] = (switch[num] + 1) % 2
      else:
        switch[num-i] = (switch[num-i] + 1) % 2
        switch[num+i] = (switch[num+i] + 1) % 2

for i in range(1, N+1):
  print(switch[i], end=' ')
  if i % 20 == 0: print()