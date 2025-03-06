# https://www.acmicpc.net/problem/12789

# 내 답안
# 걸린 시간: 56ms
# 후에 stack 따로 처리 안 하고 구현하는 방법 -> 첫 번째 조건문 안에서 numbers[0]과 비교 후 stack[-1]과 비교하기.
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
stack = deque()
now_number = 1
ind = 0
while ind < N:
  if numbers[ind] != now_number:
    if stack and now_number == stack[-1]:
      stack.pop()
      now_number += 1
    elif (stack and now_number != stack[-1]) or not stack:
      stack.append(numbers[ind])
      ind += 1
  else:
    now_number += 1
    ind += 1

while stack:
  if now_number != stack.pop():
    print("Sad")
    break
  else: now_number += 1
else:
  print("Nice")