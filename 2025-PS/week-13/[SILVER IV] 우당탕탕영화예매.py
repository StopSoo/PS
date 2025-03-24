# https://www.acmicpc.net/problem/29700

# 내 답안
# 걸린 시간: 2820ms
# 슬라이딩 윈도우 뿐만 아니라 누적합 개념도 적용해야 시간 초과 해결 가능 (!)
# 할 때마다 int형 변환하는 것보다 애초에 입력 받을 때 int형으로 바꿔놓는 게 시간 복잡도 측면에서 더 낫다. 
import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
pos = [list(map(int, list(input().strip()))) for _ in range(N)]

count = 0
for row in range(N):
  s = sum(pos[row][:K])
  if s == 0: count += 1
  for i in range(M-K):
    if s - pos[row][i] + pos[row][i+K] == 0: 
      count += 1
    s = s - pos[row][i] + pos[row][i+K] # 갱신 (!)
print(count)