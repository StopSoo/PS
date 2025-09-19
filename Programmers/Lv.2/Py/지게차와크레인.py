# https://school.programmers.co.kr/learn/courses/30/lessons/388353

# 내가 잘 구현한 포인트
# - 지게차와 크레인을 구분해서 잘 표시한 것.
# - 외부 패딩 넣은 것.
# 내가 마지막에 놓친 포인트: 외부 공기에서 BFS하는 것. -> 크레인으로 제거한 포인트를 걱정할 필요가 없음.
from collections import deque

def solution(storage, requests):
  n, m = len(storage), len(storage[0]) # 행, 열의 수
  # 패딩 추가: 외부를 -1로 표시
  new_sto = [[-1] * (m + 2)]
  for row in storage:
    new_sto.append([-1] + list(row) + [-1])
  new_sto.append([-1] * (m + 2))
  
  count = n * m  # 남은 컨테이너 수

  for req in requests:
    if len(req) == 1:  # 지게차
      for i in range(1, n + 1):
        for j in range(1, m + 1):
          if new_sto[i][j] == req:
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
              if new_sto[i+dy][j+dx] == -1:  # 외부와 접해 있으면 제거
                new_sto[i][j] = 0
                count -= 1
                break
    else:  # 크레인
      for i in range(1, n + 1):
        for j in range(1, m + 1):
          if new_sto[i][j] == req[0]:
            new_sto[i][j] = 0
            count -= 1
    # BFS로 외부 공기(-1) 확산
    H, W = n + 2, m + 2
    visited = [[False] * W for _ in range(H)] # 방문 배열 쓰세요!!
    deq = deque()
    for i in range(H):
      for j in range(W):
        if new_sto[i][j] == -1 and not visited[i][j]: # 외부 공기에서 BFS(!!)
          deq.append((i, j))
          visited[i][j] = True
          while deq:
            y, x = deq.popleft()
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
              ny, nx = y + dy, x + dx
              if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
                if new_sto[ny][nx] == 0:  # 제거된 칸을 외부로 변환
                  new_sto[ny][nx] = -1
                  deq.append((ny, nx))
                elif new_sto[ny][nx] == -1:  # 이미 외부면 계속 BFS
                  deq.append((ny, nx))
                visited[ny][nx] = True

  return count
