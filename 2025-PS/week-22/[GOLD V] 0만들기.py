# https://www.acmicpc.net/problem/7490

# 내 답안
# 걸린 시간: 144ms
# 알고리즘: 백트래킹
# 감은 잡았으나 구현 마무리가 어려웠음!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def back(n):
  if n == N:
    state.append(str(n))
    if eval(''.join(state).replace(' ', '')) == 0:
      result.append(''.join(state))
    state.pop()
    return

  state.append(str(n)) # 숫자 추가
  for oper in ['+', '-', ' ']:
    state.append(oper) # 연산자 추가
    back(n+1)
    state.pop() # 연산자 빼내기
  state.pop() # 숫자 빼내기

T = int(input())
for _ in range(T):
  N = int(input())
  result = [] # 수식들을 저장하는 배열 
  state = [] # 현재 수식을 저장하는 배열

  back(1)
  print('\n'.join(sorted(result)) + '\n')