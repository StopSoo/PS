# https://www.acmicpc.net/problem/3107

# 내 답안
# 걸린 시간: 36ms
import sys
input = sys.stdin.readline

address = input().strip().split(':')
answer = []
flag = False # ':' 처리 여부
for a in address:
  if a != '':
    answer.append('0' * (4 - len(a)) + a)
  elif a == '' and not flag:
    flag = True
    for _ in range(8 - len(set(address)) + 1):
      answer.append('0000')

print(':'.join(answer))