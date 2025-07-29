# https://www.acmicpc.net/problem/13549

# 내 답안
# 걸린 시간: 204ms
# 간선마다 가중치 값이 다르므로 BFS는 사용X. -> 다익스트라 / 플로이드-워셜을 사용해야 함.
# 새로운 위치로 이동할 때 위치 범위 체크 잘하기 (!)
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, K = map(int, input().split())

q = [(0, N)] # (누적 시간, 현재 위치)
time = [INF] * 100001
time[N] = 0
while q:
  second, pos = heapq.heappop(q)
  if pos == K:
    print(second)
    break
  
  if time[pos] < second: continue 
  for t, new_pos in [[1, pos + 1], [1, pos - 1], [0, pos * 2]]:
    if (0 <= new_pos <= 100000) and (time[new_pos] > second + t):
      time[new_pos] = second + t # 갱신        
      heapq.heappush(q, (second + t, new_pos))