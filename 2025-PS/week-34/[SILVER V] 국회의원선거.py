# https://www.acmicpc.net/problem/1417

# 내 답안
# 걸린 시간: 40ms
# 항상 예외 처리를 잘 하자!
import heapq

N = int(input())
my_votes = int(input()) # 다솜이의 투표 수
hq = []

if N >= 1:
  for i in range(N-1):
    count = int(input())
    heapq.heappush(hq, -count)

answer = 0
if hq and my_votes <= -hq[0]:
  while True:
    count = heapq.heappop(hq)
    heapq.heappush(hq, -(-count - 1))
    answer += 1
    my_votes += 1
    if my_votes > -hq[0]: 
      break

print(answer)