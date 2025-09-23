# https://www.acmicpc.net/problem/1080

# 내 답안
# 걸린 시간: 40ms
# 알고리즘: 그리디
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

if N < 3 or M < 3:
  # 무조건 -1인 게 아니라 두 배열이 같은지를 체크한 후 결과를 출력
  flag = True
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        flag = False
        break
    if not flag: break
  if not flag:
    print(-1)
  else: 
    print(0)
else:
  # 왼쪽 상단 원소를 기준으로 비교하는 것이 그리디다.
  # 지금 해결할 수 있는 차이는 지금 해결한다. 
  count = 0
  for i in range(N - 2):
    for j in range(M - 2):
      if A[i][j] != B[i][j]:
        count += 1
        for k in range(3):
          for l in range(3):
            if A[i+k][j+l] == 0: A[i+k][j+l] = 1
            else: A[i+k][j+l] = 0
  
  flag = True
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        flag = False
        break
    if not flag: break
  
  print(count if flag else -1)