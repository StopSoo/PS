# https://www.acmicpc.net/problem/18258

# 내 답안
# 걸린 시간: 1392ms
# queue 불러오기: import queue로 불러오고, queue.Queue()로 사용하기 (!)
# 근데 결국 queue가 인덱싱이 안돼서 deque 사용함 ㅋㅋ
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
q = deque()
for _ in range(N):
  order = input().strip().split()
  if order[0] == "push":
    q.append(int(order[1]))
  elif order[0] == "pop":
    print(str(q.popleft()) + '\n' if q else '-1\n')
  elif order[0] == "size":
    print(str(len(q)) + '\n')
  elif order[0] == "empty":
    print('1\n' if not q else '0\n')
  elif order[0] == "front":
    print(str(q[0]) + '\n' if q else '-1\n')
  elif order[0] == "back":
    print(str(q[-1]) + '\n' if q else '-1\n')