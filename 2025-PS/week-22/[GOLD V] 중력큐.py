# https://www.acmicpc.net/problem/28078

# 내 답안
# 시간 초과 나와서 고치다가 완성 못 함.
# 거의 두 시간 동안 품 ;; 중력에 의해 떨어지는 공을 체크할 때가 어려웠음. 두 시간 동안 붙잡고 있으니까 이제 뭐가 틀린지도 모르겠음,,
# 꼭 다음에 다시 한 번 꼼꼼히 풀어보기
import sys
input = sys.stdin.readline
from collections import deque

def remove_item_under_bar():
  global b_count

  while deq:
    if up == 'f':
      pop_item = deq.popleft()
      if pop_item == 'w':
        deq.appendleft(pop_item)
        break
    else: # 뒤가 위라면
      pop_item = deq.pop()
      if pop_item == 'w':
        deq.append(pop_item)
        break
    b_count -= 1
  return

Q = int(input())
deq = deque()
direction = 'h' # h면 가로 v면 세로
up = 'f' # f면 앞이 위, b면 뒤가 위
front = 'r' # r이면 오른쪽이 앞, l이면 왼쪽이 앞
b_count = 0
w_count = 0
for _ in range(Q):
  order = input().strip()
  if order == "push b": # 세로면 가림막이 하나라도 있을 때, 가로면 그냥 공 삽입
    if direction == 'v' and w_count:
      if up == 'b':
        if front == 'r': deq.appendleft('b')
        else: deq.append('b')
    elif direction == 'h':
      if front == 'r': deq.appendleft('b')
      else: deq.append('b')
    b_count += 1
  elif order == "push w": # 가림막 삽입
    if direction == 'v':
      if up == 'f': deq.appendleft('w')
      else: deq.append('w')
    elif direction == 'h':
      if front == 'r': deq.appendleft('w')
      else: deq.append('w')
    w_count += 1
  elif order == "pop": # 공이나 가림막 하나 제거
    if front == 'r': 
      item = deq.pop()
    else: 
      item = deq.popleft()
    if item == 'b': b_count -= 1
    else: w_count -= 1
    print(direction, up, front)
    if direction == 'v': # 세로일 경우만 체크
      remove_item_under_bar() # 바 밑 공들 제거
  elif order == "rotate l": 
    if direction == 'h': # 방향 변경
      direction = 'v'
      if front == 'r': up = 'f'
      else: up == 'b'
      remove_item_under_bar() # 바 밑 공들 제거 
    else: 
      direction = 'h'
      if up == 'f': front = 'b'
      else: front = 'r'
  elif order == "rotate r":
    if direction == 'h': # 방향 변경
      direction = 'v' 
      if front == 'r': up = 'b'
      else: up = 'f'
      remove_item_under_bar() # 바 밑 공들 제거
    else: 
      direction = 'h'
      if up == 'f': front = 'r'
      else: front = 'b'
  elif order == "count b": print(b_count) # 공 개수 출력
  elif order == "count w": print(w_count) # 가림막 개수 출력
  print(deq)

# 구글링 코드
# 걸린 시간: 532ms
# state를 0123, 이렇게 네 방향으로 구분해놓은 게 명확하고 좋은 것 같음.
# 또한 애초에 명령 받을 때 리스트로 받아서 조건문 분기한 것도 깔끔한 것 같음.
from collections import deque
import sys
input = sys.stdin.readline

state = 0 # 방향(동남서북)
counts = [0, 0] # (b, w)
Q = deque()
for _ in range(int(input())):
  cmd = input().split()

  if cmd[0] == 'pop' and Q:
    counts[Q.pop()] -= 1
  elif cmd[0] == 'push':
    if cmd[1] == 'b':
      Q.appendleft(0)
      counts[0] += 1
    else:
      Q.appendleft(1)
      counts[1] += 1
  elif cmd[0] == 'rotate':
    if cmd[1] == 'l':
      state = (state - 1) % 4
    else:
      state = (state + 1) % 4
  # 중력 시뮬레이션 (!)
  if state % 2:
    while Q:
      if state == 1: # 큐가 아래를 보고 있을 때
        if Q[-1] == 1: break 
        else:
          Q.pop()
          counts[0] -= 1
      elif state == 3:
        if Q[0] == 1: break
        else:
          Q.popleft()
          counts[0] -= 1
  
  if cmd[0] == 'count':
    if cmd[1] == 'b': print(counts[0])
    else: print(counts[1])