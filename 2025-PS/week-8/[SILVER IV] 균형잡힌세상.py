# https://www.acmicpc.net/problem/4949

# 내 답안
# 걸린 시간: 260ms
# 처음 풀 때 놓쳤던 부분: 짝이 맞는다는 것은 문자열을 다 돌았을 때 deque가 비어있다는 뜻 (!)
from collections import deque

while True:
  sentence = input()
  if not sentence.endswith('.'): # 문자열이 온점으로 끝나야 한다는 조건
    print("no")
    continue
  if sentence == ".": break # 온점만 입력하면 반복문 종료

  deq = deque() # deque 초기화
  for s in sentence: # deque에는 (, ), [, ]만 넣기
    if s == '(' or s == '[': deq.append(s)
    elif s == ')':
      if len(deq) == 0 or deq[-1] != '(':
        print("no")
        break
      else: deq.pop()
    elif s == ']':
      if len(deq) == 0 or deq[-1] != '[':
        print("no")
        break
      else: deq.pop()
  else:
    if len(deq) == 0: print("yes")
    else: print("no")