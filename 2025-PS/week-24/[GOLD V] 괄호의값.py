# https://www.acmicpc.net/problem/2504

# 답안
# 걸린 시간:
# 풀다가 중첩 괄호 해결 방법을 모르겠어서 막혔음 ㅜ.ㅜ temp 변수를 활용하는 방법을 잘 익혀놓을 것(!)
import sys
input = sys.stdin.readline

word = input().strip()
stack = []
answer = 0 # 총합
temp = 1 
for i in range(len(word)):
  w = word[i]

  if w == '(':
    stack.append(w)
    temp *= 2
  if w == '[': 
    stack.append(w)
    temp *= 3
  elif w == ')':
    if not stack or stack[-1] != '(':
      answer = 0
      break
    if word[i-1] == '(': # 바로 닫히는 경우만 더해줌
      answer += temp
    stack.pop()
    temp //= 2 # 괄호를 닫았으니 temp 원상복귀
  elif w == ']':
    if not stack or stack[-1] != '[':
      answer = 0
      break
    if word[i-1] == '[': # 바로 닫히는 경우만 더해줌
      answer += temp
    stack.pop()
    temp //= 3 # 괄호를 닫았으니 temp 원상복귀

print(answer if not stack else 0)