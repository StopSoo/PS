# https://www.acmicpc.net/problem/6588

# 내 답안
# 걸린 시간: 3108ms(python3) / 504ms(pypy3)
import math
import sys
input = sys.stdin.readline

def find_primes(n): # 에라토스테네스의 체
  checked = [0, 0] + [1] * (n-1)
  for i in range(2, int(math.sqrt(n))+1):
    for j in range(i*i, n+1, i):
      checked[j] = 0
  return checked

primes = find_primes(1000000)
while True:
  n = int(input())
  if n == 0: break
  answer = 0
  for i in range(3, n//2+1, 2): # 홀수만 체크
    if primes[i] and primes[n-i]:
      print(n, "=", i, "+", n-i)
      break
  else: print("Goldbach's conjecture is wrong.")