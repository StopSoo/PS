# https://www.acmicpc.net/problem/15665

# 내 답안
# 걸린 시간: 2752ms
# 백트래킹을 활용한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = sorted(list(map(int, input().strip().split())))
ans = []

answer = []
def back():
  if len(answer) == M:
    ans.append(answer[:]) # 리스트 복사해서 넣기 (!)
    return
  for number in numbers:
    answer.append(number)
    back()
    answer.pop()

back()
unique_ans = sorted(list(map(list, set(map(tuple, ans)))))
for a in unique_ans:
  print(*a)