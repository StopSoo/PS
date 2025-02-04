# https://www.acmicpc.net/problem/10828

# 내 답안
# 빠른 표준 입출력 (!!!)
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
stack = []

for _ in range(N):
  order = input().strip() # 입력 시 개행 문자 제거
  if order.startswith("push"): stack.append(order.split()[1])
  elif order == "top": print(stack[-1]+'\n' if stack else '-1\n') # 모든 print문에 개행문자 추가
  elif order == "size": print(str(len(stack))+'\n')
  elif order == "empty": print('1\n' if len(stack) == 0 else '0\n')
  elif order == "pop":
    if stack: print(str(stack.pop())+'\n')
    else: print('-1\n')