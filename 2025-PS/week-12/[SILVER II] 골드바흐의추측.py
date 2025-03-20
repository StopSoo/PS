# https://www.acmicpc.net/problem/9020

# 내 답안
# 걸린 시간: 1528ms(python3) / 196ms(pypy3)
import math
def find_primes(n): # 에라토스테네스의 체
  checked = [0, 0] + [1] * (n-1)
  for i in range(2, int(math.sqrt(n))+1):
    for j in range(i*i, n+1, i):
      checked[j] = 0
  return checked

T = int(input())
numbers = [int(input()) for _ in range(T)]
primes = find_primes(max(numbers))

for i in range(T):
  n = numbers[i]
  max_num = 0
  for j in range(2, n//2+1): # 절반까지만 돌기 (!)
    if primes[j] == 1 and primes[n-j] == 1: max_num = j
  print(max_num, n - max_num)
