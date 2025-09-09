# https://www.acmicpc.net/problem/13172

# 답안
# 걸린 시간: 112ms
# 알고리즘: 수학, 정수론, 분할정복을 이용한 거듭제곱
import sys
input = sys.stdin.readline

MOD = 1000000007

M = int(input())

def cal(N, x):
  if x == 1:
    return N
  v = cal(N, x // 2)
  if x % 2 == 0:
    return v * v % MOD
  else:
    return v * v * N % MOD

count = 0
for i in range(M):
  N, S = map(int, input().split())
  rN = cal(N, MOD-2)
  count = (count + rN * S % MOD) % MOD

print(count)