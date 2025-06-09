# https://www.acmicpc.net/problem/2167

# 내 답안
# 걸린 시간: 152ms
# 문제의 배열은 인덱스가 1부터 시작하기 때문에 그 부분을 고려해서 코드를 수정하면 좀 더 직관적일 듯 !!

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = list(list(map(int, input().strip().split())) for _ in range(N))
for i in range(N):
  for j in range(M):
    if 0 <= i - 1 < N - 1: numbers[i][j] += numbers[i-1][j]
    if 0 <= j - 1 < M - 1: numbers[i][j] += numbers[i][j-1]
    if (0 <= i - 1 < N - 1) and (0 <= j - 1 < M - 1): numbers[i][j] -= numbers[i-1][j-1]

K = int(input())
for _ in range(K):
  i, j, x, y = map(int, input().strip().split())
  result = numbers[x-1][y-1]
  if 0 <= j - 2 < M - 1: result -= numbers[x-1][j-2]
  if 0 <= i - 2 < N - 1: result -= numbers[i-2][y-1]
  if (0 <= i - 2 < N - 1) and (0 <= j - 2 < M - 1): result += numbers[i-2][j-2]
  print(result)