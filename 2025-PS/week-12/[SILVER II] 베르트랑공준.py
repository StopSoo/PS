# https://www.acmicpc.net/problem/4948

# 내 답안
# 걸린 시간: 656ms
# 에라토스테네스의 체 할 때 체크 배열 그대로 리턴해서 1, 0 여부 확인하는 게 시간복잡도 측면에서 더욱 좋음 (!)
# 카운트 셀 때 sum(primes[n+1:n*2+1])로 하면 시간복잡도 측면에서 더욱 좋음 (!)
import math

def find_primes(n): # 에라토스테네스의 체
  checked = [0, 0] + [1] * (n-1)
  for i in range(2, int(math.sqrt(n))+1):
    for j in range(i*i, n+1, i):
      checked[j] = 0
  return checked

primes = find_primes(246912)
while True:
  n = int(input())
  if n == 0: break
  count = 0
  for num in range(n+1, n*2 + 1):
    if primes[num] == 1: count += 1
  print(count)
