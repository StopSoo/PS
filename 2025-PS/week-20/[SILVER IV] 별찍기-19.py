# https://www.acmicpc.net/problem/10994

# 내 답안
# 걸린 시간: 44ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def make_star(n):
  # base-case
  if n == 1:
    return ['*']
  
  star = make_star(n-1)
  A = []

  A.append('*' * (1 + 4*(n-1)))
  A.append('*' + ' '*(4*(n-1)-1) + '*')
  for i in star:
    A.append('* ' + i + ' *')
  A.append('*' + ' '*(4*(n-1)-1) + '*')
  A.append('*' * (1 + 4*(n-1)))

  return A

N = int(input())
print('\n'.join(make_star(N)))