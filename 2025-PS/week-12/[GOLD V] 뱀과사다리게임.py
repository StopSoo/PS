# https://www.acmicpc.net/problem/16928

# 답안
# 걸린 시간: 72ms
# 1시간 넘게 집중해서 풀었는데 계속 이게 맞나? 생각만 듬
# BFS를 이용했으니 무조건 최소 횟수를 보장. 시간 복잡도는 O(1)
from collections import deque

N, M = map(int, input().split())
bridges = {a: b for _ in range(N) for a, b in [map(int, input().split())]}
hell = {a: b for _ in range(M) for a, b in [map(int, input().split())]}

deq = deque([(1, 0)]) # (현재 위치, 카운트)
visited = [False] * 101 # 1 ~ 100의 방문 여부 체크
visited[1] = True # 시작점 방문 체크
while deq:
  pos, count = deq.popleft()
  if pos == 100:
    print(count)
    break

  for i in range(1, 7): # 주사위 굴리기
    new_pos = pos+i
    if new_pos > 100: break
    # 사다리나 뱀을 만나면 따라가기
    if new_pos in bridges:
      new_pos = bridges[new_pos]
    elif new_pos in hell:
      new_pos = hell[new_pos]
    # 방문한 적 없으면 큐에 추가
    if not visited[new_pos]:
      visited[new_pos] = True
      deq.append((new_pos, count+1))