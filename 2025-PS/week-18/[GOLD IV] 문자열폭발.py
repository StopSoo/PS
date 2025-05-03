# https://www.acmicpc.net/problem/9935

# 내 답안
# 걸린 시간: 824ms -> 472ms
# 자료구조: 스택
# words[i] == bomb[-1] 조건을 추가했더니 시간 절감됨 (!)
import sys
input = sys.stdin.readline

words = input().strip()
bomb = input().strip()
stack = []
for i in range(len(words)):
  stack.append(words[i])
  if words[i] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
    for _ in range(len(bomb)): stack.pop()
print(''.join(stack) if stack else 'FRULA')