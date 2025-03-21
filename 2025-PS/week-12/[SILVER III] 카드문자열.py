# https://www.acmicpc.net/problem/13417

# 내 답안
# 걸린 시간: 104ms
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  n = int(input())
  answer = '' # 제출할 정답
  cards = deque(input().strip().split())
  while cards:
    if answer == '':
      answer += cards.popleft()
    else:
      if ord(answer[0]) >= ord(cards[0]):
        answer = cards.popleft() + answer
      else:
        answer = answer + cards.popleft()
  print(answer)