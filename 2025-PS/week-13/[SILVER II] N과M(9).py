# https://www.acmicpc.net/problem/15663

# 내 답안
# 걸린 시간: 184ms
# 백트래킹을 활용한 코드
# 방문 체크 배열을 둔 이유 -> 주어진 리스트에 동일한 숫자가 2개 이상일 경우를 체크.
# 이차원 배열의 중복 제거 -> 리스트 내부 리스트들을 모두 튜플로 변경한 후 set()화 하기. 
# 다른 사람 답안 보니까, 그냥 permutations 사용하면서 같은 숫자가 2개 이상 있을 경우를 대비하여 set()화하는 것도 해결책일 수 있음 (!)
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
    # 중복 허용 X / 같은 숫자, 다른 위치 값을 넣을 때를 체크.
    if (not answer) or (number not in answer) or (number in answer and not visited[i]):
      answer.append(number)
      visited[i] = True
      back()
      visited[i] = False
      answer.pop()

back()
unique_ans = sorted(list(map(list, set(map(tuple, ans))))) # 중복 제거
for a in unique_ans:
  print(*a, sep=' ')