# https://www.acmicpc.net/problem/10845

# 내 답안
# 걸린 시간: 64ms
# 첫 코드에서는 빠른 입출력을 안 써서 '시간 초과'가 났었음
# order = input().strip()에서 바로 split() 해주면 order가 리스트 형태가 되므로 인덱싱해서 사용 가능 (!)
# 경우마다 예외 처리할 때 try-except를 사용해도 된다는 걸 기억하기 (!)
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

deq = deque()
N = int(input().strip())
for _ in range(N):
  order = input().strip()
  if order.startswith("push"): 
    order, value = order.split()
    deq.append(int(value))
  elif order == "pop": print(str(deq.popleft()) + '\n' if deq else '-1\n')
  elif order == "size": print(str(len(deq)) + '\n')
  elif order == "empty": print('1\n' if not deq else '0\n')
  elif order == "front": print(str(deq[0]) + '\n' if deq else '-1\n')
  elif order == "back": print(str(deq[-1]) + '\n' if deq else '-1\n')