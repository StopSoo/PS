# https://www.acmicpc.net/problem/2448

# 내 답안
# 걸린 시간: 96ms
# 알고리즘: 재귀
# 재귀를 잘 익히자 !! 기본 케이스에 집중해보자 !!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def make_star(n):
  # base-case
  if n == 3:
    return ['  *  ', ' * * ', '*****']

  star = make_star(n//2)
  A = []

  for i in star:
    A.append(' '*(n//2) + i + ' '*(n//2))
  for i in star:
    A.append(i + ' ' + i)
  
  return A

N = int(input())
print('\n'.join(make_star(N)))