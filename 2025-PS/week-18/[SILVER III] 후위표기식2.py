# https://www.acmicpc.net/problem/1935

# 내 답안
# 걸린 시간: 56ms
# pop하는 숫자들의 순서를 잘 체크할 것.
# eval() 함수 사용할 때 주의하기.
from collections import deque

N = int(input())
operation = input()
numbers = list(int(input()) for _ in range(N))
deq = deque()
for oper in operation:
  if oper.isalpha(): deq.append(numbers[ord(oper)-65])
  elif not oper.isalpha(): # 알파벳이 아니라면(연산자가 나온다면)
    n2 = deq.pop()
    n1 = deq.pop()
    deq.append(eval(f"{n1}{oper}{n2}"))

print(f"{deq[0]:.2f}")