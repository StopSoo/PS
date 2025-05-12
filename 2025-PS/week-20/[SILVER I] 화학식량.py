# https://www.acmicpc.net/problem/2257

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 스택
import sys
input = sys.stdin.readline

dt = {'H': 1, 'C': 12, 'O': 16}
word = input().strip()
stack = []
temp = 0 # 괄호 안 식 계산값
for ch in word:
  if ch == '(': stack.append(ch)
  elif ch.isalpha(): stack.append(dt[ch])
  elif ch.isdigit():
    pop_ch = stack.pop()
    stack.append(pop_ch * int(ch))
  elif ch == ')':
    while True:
      pop_ch = stack.pop()
      if pop_ch == '(': break
      temp += pop_ch
    stack.append(temp)
    temp = 0

print(sum(stack))