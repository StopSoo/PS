# https://www.acmicpc.net/problem/2581

# 내 답안
import math

def find_prime(s, e): # 에라토스테네스의 체
  is_prime = [0, 0] + [1] * (e-1)
  for i in range(2, int(math.sqrt(e))+1):
    for j in range(i*i, e+1, i):
      is_prime[j] = 0
  return [idx for idx, num in enumerate(is_prime) if num == 1 and s <= idx <= e]

M = int(input())
N = int(input())

prime_numbers = find_prime(M, N) # M 이상 N 이하 범위 내 소수 구하기
if len(prime_numbers) == 0: print(-1)
else:
  print(sum(prime_numbers))
  print(prime_numbers[0])