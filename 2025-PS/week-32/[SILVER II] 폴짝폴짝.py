# https://www.acmicpc.net/problem/1326

# 내 답안
# 걸린 시간: 76ms
# 알고리즘: 그래프 탐색
# 인덱스를 잘 체크하자!
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
numbers = [0] + list(map(int, input().strip().split()))
a, b = map(int, input().strip().split())

deq = deque([(a, 0)])
checked = [0] * (N + 1)
checked[a] = 1
while deq:
  now, count = deq.popleft()
  if now == b:
    print(count)
    break

  for i in range(now + numbers[now], N + 1, numbers[now]): # 앞으로 가기
    if not checked[i]:
      checked[i] = 1
      deq.append((i, count + 1))
  for i in range(now - numbers[now], 0, -numbers[now]):
    if not checked[i]:
      checked[i] = 1
      deq.append((i, count + 1))
else:
  print(-1)