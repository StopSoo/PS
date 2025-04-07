# https://www.acmicpc.net/problem/14490

# 내 답안
# 걸린 시간: 36ms
import math

a, b = map(int, input().split(':'))
print(str(a // math.gcd(a, b)) + ":" + str(b // math.gcd(a, b)))

# 유클리드 호제법을 이용하기
def gcd(n, m):
  while m > 0:
    n, m = m, n % m

	return n

a, b = map(int, input().split(':'))
g = gcd(a, b)
print(str(a // g) + ":" + str(b // g))