# https://www.acmicpc.net/problem/2018

# 내 답안
# 걸린 시간: 
# 알고리즘: 투포인터
# 메모리가 32MB 제한이세요 ㅋㅋ
import sys
input = sys.stdin.readline

N = int(input().strip())

ways = 0
i, j = 1, 1
now = 1
while i <= N:
  if now < N:
    j += 1
    now += j
  elif now == N:
    now -= i
    i += 1
    ways += 1
  else:
    now -= i
    i += 1

print(ways)