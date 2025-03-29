# https://www.acmicpc.net/problem/15664

# 내 답안
# 걸린 시간: 36ms
# 백트래킹을 활용한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = sorted(list(map(int, input().strip().split())))
ans = []

answer = []
visited = [False] * N # 방문 체크 배열
def back():
  if len(answer) == M:
    ans.append(answer[:])
    return
  for i, number in enumerate(numbers):
    # 중복 허용 X / 비내림차순 / 같은 숫자, 다른 위치 값을 넣을 때를 체크.
    if (not answer) or (number not in answer and number >= answer[-1]) or (number in answer and not visited[i] and number >= answer[-1]):
      answer.append(number)
      visited[i] = True
      back()
      visited[i] = False
      answer.pop()

back()
unique_ans = sorted(list(map(list, set(map(tuple, ans)))))
for a in unique_ans:
  print(*a, sep=' ')