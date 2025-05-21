# https://www.acmicpc.net/problem/12919

# 내 답안
# 걸린 시간: 60ms
# 아이디어 1) 문제의 방향과 반대로 T -> S로 접근하는 게 포인트 (!)
# 아이디어 2) B는 시작이 B일 때를 고려하는 게 맞음 !!
import sys
input = sys.stdin.readline
from collections import deque

S = input().strip()
T = input().strip()

deq = deque([T])
while deq:
  word = deq.popleft()
  if word == S:
    print(1)
    break

  if len(word) > len(S):
    if word[-1] == 'A': # 끝이 A면
      deq.append(word[:-1]) # 뒤에 A를 추가하는 연산을 했을 것.
    if word[0] == 'B': # 시작이 B면
      deq.append(word[1:][::-1]) # 뒤에 B를 추가하고 뒤집는 연산을 했을 것.
else:
  print(0)