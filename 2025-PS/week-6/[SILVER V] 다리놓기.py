# https://www.acmicpc.net/problem/1010

# 내 답안
# 15분 정도 걸림
# combinations가 너무 느림 -> 시간 초과
# from itertools import combinations
from math import factorial

T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  N, M = max(N, M), min(N, M)
  # for comb in combinations(list(range(max(N, M))), min(N, M)): count += 1
  # print(len(list(combinations(list(range(max(N, M))), min(N, M)))))
  print(factorial(N) // (factorial(N-M) * factorial(M))) # 분모에 괄호 쳐주기 (!)