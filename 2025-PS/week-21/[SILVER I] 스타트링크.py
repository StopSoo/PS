# https://www.acmicpc.net/problem/5014

# 내 답안
# 걸린 시간: 756ms
# 첫 코드 때 BFS인데 왜 방문 체크 배열을 안 쓰신 건지 ~ (시간 초과 났었음)
# BFS에서는 큐에 값을 넣을 때 방문 체크를 해야 함 (!)
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1) # 방문 체크 배열
deq = deque([(S, 0)]) # (현재 위치, 이동 횟수)
visited[S] = True    
while deq:
  now, count = deq.popleft()
  if now == G:
    print(count)
    break
  
  if now + U <= F and not visited[now + U]: 
    deq.append((now + U, count + 1))
    visited[now + U] = True
  if now - D >= 1 and not visited[now - D]: 
    deq.append((now - D, count + 1))
    visited[now - D] = True
else: print("use the stairs")