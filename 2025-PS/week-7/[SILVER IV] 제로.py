# https://www.acmicpc.net/problem/10773

# 내 답안
K = int(input())
stack = []
for _ in range(K):
  number = int(input())
  if number == 0: stack.pop()
  else: stack.append(number)
print(sum(stack))