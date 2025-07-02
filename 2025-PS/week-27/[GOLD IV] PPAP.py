# https://www.acmicpc.net/problem/16120

# 내 답안
# 걸린 시간: 504ms
# 첫 코드 때는 replace를 사용했는데 시간초과가 남.
# 스택을 써서 PPAP가 완성되면 빼내는 식으로 코드 변경.
import sys
input = sys.stdin.readline

word = input().strip()
stack = []
for i in range(len(word)):
  stack.append(word[i])
  if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
    for _ in range(4): stack.pop()
    stack.append("P")

if stack == ['P']: print("PPAP")
else: print("NP")