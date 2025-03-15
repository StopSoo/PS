# https://www.acmicpc.net/problem/17103

# 내 답안
# 걸린 시간: 3140ms (python3) / 220ms (pypy3)
import math

def find_number(n): # 에라토스테네스의 체
  numbers = [0, 0] + [1] * (n-1)
  for num in range(2, int(math.sqrt(n))+1): # int(루트n) + 1까지인 것 (!)
    if numbers[num] == 0: continue
    else:
      for i in range(num*num, n+1, num): numbers[i] = 0 # num*num부터 시작해도 되는 것 (!)
  return numbers

T = int(input())
checks = [int(input()) for _ in range(T)]
primes = find_number(max(checks)) # 에라토스테네스의 체는 한 번만 해서 배열을 구해놓는 것.

for i in range(T):
  count = 0
  for j in range(2, checks[i]//2 + 1): # 절반까지만 도는 것 (!)
    if primes[j] == 1 and primes[checks[i]-j] == 1: count += 1 # O(1)
  print(count)