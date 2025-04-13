# https://www.acmicpc.net/problem/1946

# 내 답안
# 걸린 시간: 5300ms (python3) / 4504ms (pypy3)
# 시간 초과의 원인은 이중 for문!!
import sys
input = sys.stdin.readline

T = int(input())
answers = [] # 정답 배열
for _ in range(T):
  N = int(input())
  scores = sorted([list(map(int, input().strip().split())) for _ in range(N)]) # 서류 순위로 정렬

  count = 0
  min_score = scores[0][1] # 1등 지원자의 면접 점수
  for i in range(N):
    if scores[i][1] <= min_score: # 어차피 서류 순위로 정렬되어 있으므로 이 방식이 굿.
      count += 1
      min_score = scores[i][1]
  answers.append(count)

print(*answers, sep='\n')