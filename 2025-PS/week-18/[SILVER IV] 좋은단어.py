# https://www.acmicpc.net/problem/3986

# 내 답안
# 걸린 시간: 104ms
# 이 문제를 읽고 스택이라는 생각을 하는 것이 1차 문제!!
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for _ in range(N):
  stack = []
  word = input().strip()
  for w in word:
    if stack and stack[-1] == w: stack.pop()
    else: stack.append(w)
  if not stack: answer += 1

print(answer)