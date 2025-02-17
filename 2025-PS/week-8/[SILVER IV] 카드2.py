# https://www.acmicpc.net/problem/2164

# 내 답안
# 걸린 시간: 172ms
# deque를 활용한 답안
# 1)append와 pop 모두 O(1)으로 연산 가능
# 2) deque를 선언할 때 값 초기화 가능
# 3) len 사용 가능
# 4) pop(): 가장 오른쪽 값 제거 및 반환 / popleft(): 가장 왼쪽 값 제거 및 반환
# 5) indexing 가능
from collections import deque

N = int(input())
deq = deque([num for num in range(1, N+1)])

while len(deq) != 1:
  deq.popleft()
  deq.append(deq.popleft())
print(deq[0])