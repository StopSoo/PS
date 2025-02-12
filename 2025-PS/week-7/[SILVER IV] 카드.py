# https://www.acmicpc.net/problem/1835
# 힌트 7 [4]
# 힌트 6 [3,4]
# 힌트 5 [3,4]->[4,3]->[3,4]->[4,3]
# 힌트 4 [2,4,3]
# 힌트 3 [2,4,3]->[3,2,4]->[4,3,2]
# 힌트 2 [1,4,3,2]
# 힌트 1 [2,1,4,3]

# 내 답안
# 처음에 문제 이해가 안됐음 ...
# insert(넣을 인덱스, 값): 원하는 자리에 값 넣기 가능
N = int(input())
cards = [N] # N번 카드만 남아있는 상태
cur_num = N-1

while len(cards) != N:
  cards.insert(0, cur_num)
  # cur_num 값 만큼 맨 뒤 카드를 빼서 앞으로 가져오기
  for i in range(cur_num):
    pop_num = cards.pop()
    cards.insert(0, pop_num)
  cur_num -= 1
print(*cards)

# deque를 사용한 답안
# deque에는 appendleft가 있다 (!)
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
dq = deque()
dq.append(N)

for i in range(N - 1, 0, -1):
  dq.appendleft(i)

  for j in range(i):
    dq.appendleft(dq.pop())

print(*dq)

# deque를 사용한 다른 답안
# deque에는 rotate()를 통한 리스트 회전이 있다 (!)
# rotate(값): 양수면 오른쪽 회전, 음수면 왼쪽 회전 
from collections import *

def solve():
  n = int(input())
  arr = deque()
  
  for i in reversed(range(1, n + 1)):
    arr.appendleft(i)
    arr.rotate(i)
  
  print(*arr)

solve()