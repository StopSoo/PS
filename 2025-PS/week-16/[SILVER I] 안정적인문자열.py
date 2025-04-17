# https://www.acmicpc.net/problem/4889

# 내 답안
# 걸린 시간: 60ms
import sys
input = sys.stdin.readline
from collections import deque 

answers = []
while True:
  word = input().strip()
  count = 0 # 연산 횟수
  if word[0] == '-': break
  # 전처리하기 -> 불안정적인 문자열만 남기기
  deq = deque()
  for ch in word:
    if ch == '{':
      deq.append(ch)
    else: # '}'
      if deq and deq[-1] == '{': deq.pop()
      else: deq.append(ch)

  while deq:
    if deq[0] == '}' and deq[1] == '}' or deq[0] == '{' and deq[1] == '{':
      count += 1
      deq.popleft()
      deq.popleft()
    elif deq[0] == '}' and deq[1] == '{':
      count += 2
      deq.popleft()
      deq.popleft()
  
  answers.append(count)      

for i in range(1, len(answers)+1):
  print(f'{i}. {answers[i-1]}')