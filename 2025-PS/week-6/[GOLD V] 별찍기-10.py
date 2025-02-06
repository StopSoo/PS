# https://www.acmicpc.net/problem/2447

# 참고해서 푼 답안
# 재귀, 분할정복
def draw_stars(n):
  if n == 1: return ['*'] # basic

  stars = draw_stars(n // 3) # recursion
  result = []
  # repeat
  for star in stars:
    result.append(star * 3)
  for star in stars:
    result.append(star + ' '*(n // 3) + star)
  for star in stars:
    result.append(star * 3)
  return result

N = int(input()) # 3의 거듭제곱
print('\n'.join(draw_stars(N)))