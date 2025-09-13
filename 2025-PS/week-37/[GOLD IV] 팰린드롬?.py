# https://www.acmicpc.net/problem/10942

# 내 답안
# 걸린 시간: 2160ms(python3) / 624ms(pypy3)
# 알고리즘: DP

# 풀이 아이디어
# 1. dp[i][j]: 인덱스 i부터 j까지의 문자열이 팰린드롬이다 (!)
# 2. 길이 1 -> 길이 2 -> 길이 3 ... 순으로 채워나가기 
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [0] + list(map(int, input().strip().split()))

dp = [[False] * (N + 1) for _ in range(N + 1)]
for length in range(1, N + 1):
  for i in range(1, N - length + 2):
    j = i + length - 1
    if length == 1:
      dp[i][j] = True
    elif length == 2:
      dp[i][j] = (numbers[i] == numbers[j])
    else:
      dp[i][j] = (numbers[i] == numbers[j]) and dp[i+1][j-1]

M = int(input())
for _ in range(M):
  s, e = map(int, input().strip().split())
  if dp[s][e]: print(1)
  else: print(0)