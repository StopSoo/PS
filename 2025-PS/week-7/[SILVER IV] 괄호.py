# https://www.acmicpc.net/problem/9012

# 내 답안
T = int(input())
words = [input() for _ in range(T)]
answers = []
for word in words:
  stack = []
  flag = True
  for w in word:
    if w == "(": stack.append("(")
    else: 
      if stack: stack.pop()
      else:
        flag = False
        break
  answers.append("NO" if (not flag or stack) else "YES")
for ans in answers: print(ans)