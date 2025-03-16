# https://www.acmicpc.net/problem/11653

# 내 답안
# 걸린 시간: 1852ms (pypy3)
# 내가 너무 어렵게 품 ㅋㅋㅋ
import math
import sys
print = sys.stdout.write

def find_primes(n): # 에라토스테네스의 체
  primes = [0, 0] + [1] * (n-1)
  for i in range(2, int(math.sqrt(n))+1): # int(루트 n) + 1까지 돌리는 것 !!
    if primes[i] == 1:
      for j in range(i*i, n+1, i): primes[j] = 0
  return [idx for idx, number in enumerate(primes) if number == 1]

N = int(input())
primes = find_primes(N)

for prime in primes:
  while N % prime == 0:
    N //= prime
    print(str(prime) + '\n')
    if N == 1: break

# 좀 더 간결한 답안
N = int(input())

if N == 1: print('')
for i in range(2, N+1):
  if N%i == 0:
    while N%i == 0: # 어차피 이 과정을 거치기 떄문에 소수를 체크할 필요가 없음 (!)
      print(i)
      N /= i