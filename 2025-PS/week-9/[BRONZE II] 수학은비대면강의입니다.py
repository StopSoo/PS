# https://www.acmicpc.net/problem/19532

# 내 답안
# 걸린 시간: 32ms
# 크래머의 공식 사용 -> 행렬식을 이용한 공식
# ax + by = c
# dx + ey = f
# x = (ce - bf) / (ae - bd)
# y = (af - cd) / (ae - bd)
import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().strip().split())
det = a*e - b*d # 행렬식 계산
if det != 0: # 유일한 해가 존재하는 경우
  x = (c*e - b*f) / det
  y = (a*f - c*d) / det
  print(int(x), int(y))
