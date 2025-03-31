# https://www.acmicpc.net/problem/9465

# 내 답안
# 걸린 시간: 628ms
# 점화식을 어떻게 짜야 할지 감도 못 잡았어서, https://www.acmicpc.net/board/view/105378를 참고 !!
# scores[0][i]: i번째 열에서 위쪽 행에 해당하는 스티커를 택했을 때, 그 이전에 선택한 스티커들의 점수 합의 최댓값.
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  n = int(input().strip())
  scores = [list(map(int, input().strip().split())) for _ in range(2)]
  if n == 1: # 1인 경우도 고려하기 (!)
    print(max(scores[0][0], scores[1][0]))
    continue

  scores[0][1] += scores[1][0]
  scores[1][1] += scores[0][0]
  for i in range(2, n):
    scores[0][i] += max(scores[1][i-1], scores[1][i-2])
    scores[1][i] += max(scores[0][i-1], scores[0][i-2])
  print(max(scores[0][n-1], scores[1][n-1]))