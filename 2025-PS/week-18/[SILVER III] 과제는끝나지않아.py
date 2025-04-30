# https://www.acmicpc.net/problem/17952

# 내 답안
# 걸린 시간: 908ms
# 예외가 아닌 상황부터 조건문에 적용할 것. -> 예외부터 조건문에 작성하면 오류가 날 가능성이 큼(!)
# 파이썬은 함수 스코프를 사용하기 때문에, 한 조건문 안에서 선언한 변수도 다른 조건문에서 사용 가능하다.
import sys
input = sys.stdin.readline

total = int(input())
stack = []
get_score = 0
for _ in range(total):
  order = input().strip()
  if order != '0': one, score, time = map(int, order.split())
  elif order == '0' and stack: one, score, time = stack.pop()
  else: continue

  if time == 1: get_score += score
  else: stack.append([one, score, time-1])

print(get_score)