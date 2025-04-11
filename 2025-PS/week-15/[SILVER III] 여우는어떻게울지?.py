# https://www.acmicpc.net/problem/9536

# 내 답안
# 걸린 시간: 32ms
# 반복문을 도는 리스트에 대해 remove를 실행하면 기획과 안 맞을 수 있음.
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  sounds = list(input().strip().split())
  remove_list = []
  while True:
    order = input().strip()
    if order == "what does the fox say?": break
    order = order.split()
    remove_list.append(order[2])
  answer = []
  for sound in sounds:
    if sound not in remove_list:
      answer.append(sound)
  print(' '.join(answer))