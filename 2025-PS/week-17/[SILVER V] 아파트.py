# https://www.acmicpc.net/problem/32979

# 내 답안
# 걸린 시간: 920ms
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
T = int(input())
pos = deque(map(int, input().strip().split()))
failure = list(map(int, input().strip().split()))

answers = []
idx = 1
while failure:
  if idx == failure[0]:
    answers.append(pos[0])
    failure.remove(failure[0])
    idx = 1
    continue
  pos.rotate(-1)
  idx += 1
print(*answers)

# 덱을 사용하지 않고, 시간 복잡도도 낮은 코드
# 걸린 시간: 44ms
N = int(input())
T = int(input())
hands = list(map(int, input().split()))
call = list(map(int, input().split()))
loser = []
m = 0
for i in call:
  print(hands[((i+m)%(N*2))-1])
  m += i-1