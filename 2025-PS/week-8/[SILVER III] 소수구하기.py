# https://www.acmicpc.net/problem/1929

# 내 답안
# 걸린 시간: 5532ms -> 너무 오래 걸림
import math
import sys
input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().strip().split())
for num in range(M, N+1):
  if num == 1: continue
  if num == 2: 
    print(str(num) + '\n')
    continue
  for i in range(2, math.ceil(math.sqrt(num)) + 1):
    if num % i == 0: break
  else: 
    print(str(num) + '\n')

# 에라토스테네스의 체로 풀기 (!) 
# 걸린 시간: 272ms
import math

def prime_numbers(n):
  arr = [i for i in range(n+1)]
  for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == 0: continue
    for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 체크
      arr[j] = 0

  return [i for i in arr[2:] if arr[i]]

M, N = map(int, input().split())
for number in prime_numbers(N):
  if number >= M and number <= N: print(number)