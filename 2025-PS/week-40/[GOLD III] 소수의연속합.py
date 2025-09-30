# https://www.acmicpc.net/problem/1644

# 내 답안
# 걸린 시간: 1300ms
# 알고리즘: 에라토스테네스의 체 / 투포인터
# 투포인터 할 때 인덱스 범위 초과 잘 체크하기 (!)
import math

N = int(input())
# 소수 배열 구하기
is_prime = [1] * (N + 1)
is_prime[0] = is_prime[1] = 0
for number in range(2, int(math.sqrt(N)) + 1):
  if is_prime[number]:
    for i in range(number**2, N + 1, number):
      is_prime[i] = 0
# 소수 배열 정리
primes = [i for i in range(2, N + 1) if is_prime[i]]

# 투포인터
i, j = 0, 0
count = 0
lp = len(primes)
s = primes[0] if lp > 0 else 0
while i < lp and j < lp:
  if s == N:
    count += 1
    j += 1
    if j < lp:
      s += primes[j]
  elif s > N:
    s -= primes[i]
    i += 1
  elif s < N:
    j += 1
    if j < lp:
      s += primes[j]

print(count)