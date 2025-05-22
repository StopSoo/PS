# https://www.acmicpc.net/problem/2075

# 내 답안
# NXN 배열을 만드는 것 자체가 메모리 초과 (!)
import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = [[] for _ in range(N)]
for _ in range(N):
  numbers = list(map(int, input().split()))
  for i, number in enumerate(numbers): # N개의 힙에 숫자들 삽입
    heapq.heappush(hq[i], -number) # 내림차순 정렬을 위함

count = 0
flag = False
answer = 0
while True:
  max_value = max([-hq[i][0] for i in range(N)])
  for i in range(N):
    if -hq[i][0] == max_value: 
      if count != N-1:
        heapq.heappop(hq[i])
        count += 1
        break
      else:
        answer = max_value
        flag = True
        break
  if flag: break

print(answer)

# 두 번째 답안
# 2차원 배열이 아닌 1차원 배열로 구현 -> 어쨌든 NXN 배열을 만드므로 메모리 초과가 남.
import heapq

N = int(input())
b = []
for i in range(N):
  a = list(map(int, input().split()))
  for j in range(N):
    heapq.heappush(b, -a[j])

for _ in range(N-1): heapq.heappop(b)
print(-b[0])

# 세 번째 답안
# 걸린 시간: 884ms
# 자료구조: 힙
# 아이디어) N번째 큰 수니까 크기가 N인 힙을 만들자 !!
import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = [] # N 크기의 힙
for i in range(N):
  l = list(map(int, input().split()))
  for number in l:
    if not hq or len(hq) < N:
      heapq.heappush(hq, number)
    else: # N개의 수로 힙이 차있다면
      if number > hq[0]: # 새로운 수가 더 클 때만 갱신
        heapq.heappop(hq)
        heapq.heappush(hq, number)

print(hq[0])