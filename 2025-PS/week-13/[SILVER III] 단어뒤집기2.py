# https://www.acmicpc.net/problem/17413

# 내 답안
# 걸린 시간: 232ms
from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
word = input().strip()

new_word = ''
flag = False # 태그 열림 여부
for idx, w in enumerate(word):
  if w == '>':
    new_word += w
    deq.append(new_word)
    new_word = ''
    flag = False
  elif w == '<':
    flag = True
    deq.append(new_word[::-1]) # 열린 태그를 만나면 그 전까지의 문자열을 뒤집어서 저장
    new_word = w
  elif w == ' ':
    if flag: # 태그가 열려있으면 pass
      new_word += ' '
      continue 
    deq.append(new_word[::-1] + ' ')
    new_word = ''
  else:
    new_word += w
  
  if idx == len(word)-1: deq.append(new_word[::-1]) # 마지막 원소 누락 방지

while deq: print(deq.popleft(), end='')