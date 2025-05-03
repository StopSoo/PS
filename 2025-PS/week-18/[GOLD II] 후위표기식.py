# https://www.acmicpc.net/problem/1918

# 내 답안
# 걸린 시간: 32ms
# 자료 구조: 스택
# 배운 점 1: 1935_후위표기식2 문제를 풀었을 때처럼 연산자와 피연산자 모두 스택에 넣는 방식으로만 생각하고 있었음 (고정관념)
# 배운 점 2: 괄호와 연산자 사이의 우선순위를 어떻게 처리할지에 대한 고민. 처음엔 스택에 우선순위와 함꼐 넣으려고 했으나, 딕셔너리를 사용하는 방식이 좀 더 깔끔하다고 판단.
# 배운 점 3: 후위표기식이라는 방식에 맞게 피연산자는 바로 출력하고, 연산자만 스택을 통해 걸러내는 것. 
priority = {'+': 1, '-': 1, '*': 2, '/': 2} # 연산자 우선순위
origin = input()
stack = [] # 연산자를 담을 스택
for ch in origin:
  if ch.isalpha(): print(ch, end='')
  elif ch == '(': stack.append(ch) # 괄호의 시작을 인지하기 위해 (를 스택에 추가
  elif ch == ')':
    while True: # (가 나올 때까지 연산자들 pop하기
      oper = stack.pop()
      if oper == '(': break
      else: print(oper, end='')
  else:
    # 스택이 비어있지 않고 & 스택 마지막 요소가 (가 아니고 & 지금 연산자의 우선순위 "이상"인 우선순위를 가진 연산자가 스택에 있다면 빼내서 출력하기
    while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[ch]: 
      print(stack.pop(), end='')
    stack.append(ch) # 현재 연산자를 스택에 추가
# 출력
while stack:
  print(stack.pop(), end='')
print()