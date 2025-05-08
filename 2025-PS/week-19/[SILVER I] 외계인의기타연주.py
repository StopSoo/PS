# https://www.acmicpc.net/problem/2841

# 내 답안
# 걸린 시간: 828ms
# 문제를 이해하는 데 시간이 좀 걸림 ㅋㅋ
import sys
input = sys.stdin.readline

N, P = map(int, input().strip().split())
stack = [[] for _ in range(6)]
count = 0
for _ in range(N):
  line, p = map(int, input().strip().split())
  while True:
    if (not stack[line-1]) or (stack[line-1] and stack[line-1][-1] < p): 
      stack[line-1].append(p)
      count += 1
      break
    elif stack[line-1] and stack[line-1][-1] == p: break
    elif stack[line-1] and stack[line-1][-1] > p:
      while stack[line-1] and stack[line-1][-1] > p:
        stack[line-1].pop()
        count += 1

print(count)

# 좀 더 깔끔한 코드
# 걸린 시간: 648ms
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stacks = [[] for _ in range(7)] # 1 기반 인덱스
moves = 0

for _ in range(N):
  string, fret = map(int, input().split())
  while stacks[string] and stacks[string][-1] > fret:
    stacks[string].pop()
    moves += 1
  if not stacks[string] or stacks[string][-1] != fret:
    stacks[string].append(fret)
    moves += 1

print(moves)