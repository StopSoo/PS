# https://www.acmicpc.net/problem/11060

# 내 답안
# 걸린 시간: 48ms
# 많은 방법들 중 DP로 풀 것 같음 !!
# 가장 오른쪽 끝으로 갈 수 없는 경우를 어떻게 처리해야 하는지 막혔음.
N = int(input())
miro = list(map(int, input().split()))
count = [0] * N
for i in range(N):
  for jump in range(1, miro[i]+1):
    # 범위 안에 있는지 & 초기화가 안됐거나 초기화가 됐지만 기존값보다 업데이트되는 값이 더 작을 경우 업데이트
    if (i+jump < N) and (count[i+jump] == 0 or count[i+jump] != 0 and count[i+jump] > count[i] + 1): # 범위 안에 있다면
      count[i+jump] = count[i] + 1
  if i != 0 and count[i] == 0:
    print(-1)
    break
else:
  print(count[N-1])

# BFS를 활용한 답안
# 걸린 시간: 44ms
N = int(input())
maze = list(map(int, input().split()))

bfs = [float('inf')] * N
bfs[0] = 0

for idx in range(N):
  for next_idx in range(idx, min(idx + maze[idx] + 1, N)):
    bfs[next_idx] = min(bfs[idx] + 1, bfs[next_idx]) # 원래 값이랑 비교해서 최솟값으로 업데이트

if bfs[-1] == float('inf'): print(-1) # 오른쪽 끝까지 못 갔다는 뜻
else: print(bfs[-1])