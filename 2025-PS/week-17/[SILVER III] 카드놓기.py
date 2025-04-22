# https://www.acmicpc.net/problem/18115

# 내 답안
# 근데 답이 제대로 안 나옴 -> rotate를 반복하면서 오차를 낳을 수 있음.
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()
orders = list(map(int, input().strip().split()))
card = N
for order in reversed(orders):
  if not deq: 
    deq.append(card)
  else:
    if order == 1:
      deq.appendleft(card)
    elif order == 2:
      deq.rotate(-1)
      deq.appendleft(card)
      deq.rotate(1)
    elif order == 3:
      deq.rotate(1)
      deq.append(card)
      deq.rotate(-1)
  card -= 1

print(*deq)

# 다른 사람의 답안
# 걸린 시간: 760ms
# insert(위치, 값) 메서드를 잘 사용하자 !!
from collections import deque

num = int(input())
skills_list = list(map(int, input().strip().split()))
skills_list.reverse()
result_deque = deque()

for i in range(1, num+1):
  if skills_list[i] == 1:
    result_deque.appendleft(i)
  elif skills_list[i] == 2:
    result_deque.insert(1, i) # 인덱스 1 자에 i를 넣기
  else:
    result_deque.append(i)

print(*result_deque)