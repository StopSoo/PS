# https://www.acmicpc.net/problem/2493

# 내 답안
# 걸린 시간: 548ms
# 자료구조: 스택
# 처음에 작성했던 답안처럼 높이만 stack에 저장하고 index는 따로 변수로 관리하는 방식은 index와 answers 관리에 실패할 가능성이 높다.
# stack에 저장할 때 인덱스를 튜플로 같이 저장하는 방식이 안전하다 (!)
import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().strip().split()))
stack = []
answers = []
for i in range(N):
  while stack and tops[i] > stack[-1][1]:
    stack.pop()

  if not stack: answers.append(0)
  else: answers.append(stack[-1][0]) # 인덱스 저장
  
  stack.append((i+1, tops[i])) # (인덱스, 높이)

print(*answers)