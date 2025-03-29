# https://www.acmicpc.net/problem/15666

# 내 답안
# 걸린 시간: 68ms
# 백트래킹을 활용한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
ans = []

answer = []
def back():
  if len(answer) == M:
    ans.append(answer[:])
    return
  for i, number in enumerate(numbers):
    if (not answer) or (number not in answer and number > answer[-1]) or (answer and number in answer and number >= answer[-1]):
      answer.append(number)
      back()
      answer.pop()

back()
unique_ans = sorted(list(map(list, set(map(tuple, ans)))))
for a in unique_ans:
  print(*a)