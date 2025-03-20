# https://www.acmicpc.net/problem/5430

# 내 답안
# 걸린 시간: 236ms
# strip() -> lstrip()/rstrip() 적용하기
# deque.reverse()는 O(N)의 시간복잡도를 가짐(!)
# 따라서 시간 초과를 해결하기 위해 역순 여부를 따로 저장하고, 마지막에 한 번만 reverse()를 수행해줌.
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
  order = input()
  n = int(input())
  numbers = input().strip() # 배열 초기 입력
  if numbers == "[]":
    numbers = deque()
  else: numbers = deque(map(int, numbers.lstrip('[').rstrip(']').split(',')))

  pos = 'l' # flag
  for o in order:
    if o == 'R': # 역순 뒤집기
      if pos == 'l': pos = 'r'
      else: pos = 'l'
    elif o == 'D': # 맨 앞 원소 삭제
      if not numbers: 
        print("error")
        break
      else: 
        if pos == 'l': numbers.popleft()
        else: numbers.pop()
  else: # error가 아닌 경우
    if pos == 'r': numbers.reverse() # R이 홀수 개일 경우 마지막에 한 번 reverse해줌 
    print("[" + ','.join(map(str, numbers)) + "]")