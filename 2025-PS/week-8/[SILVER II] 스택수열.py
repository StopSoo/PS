# https://www.acmicpc.net/problem/1874

# 내 답안
# 걸린 시간: 180ms (5번 시도 끝에 성공)
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)] # 만들어야 하는 수열
flag = True # 해당 수열을 만들 수 있는지 여부
stack = []
answers = [] # push, pop 기호 배열
current_number = 1 # 스택에 넣을 값
for num in numbers: # 꺼내야 할 숫자
  while True:
    # 원래 코드: if num in stack -> O(N)의 시간 복잡도를 가짐
    if stack and num < current_number:
      answers.append('-')
      pop_num = stack.pop()
      if pop_num == num: break
    else:
      if num < current_number:
        flag = False
        break
      # 원래 코드: while문 돌면서 추가
      stack += [i for i in range(current_number, num+1)]
      answers += ['+' for i in range(current_number, num+1)]
      current_number += (num+1 - current_number)

if flag: print(*answers, sep='\n')
else: print("NO")