# https://www.acmicpc.net/problem/9375

# 내 답안
# 걸린 시간: 32ms
# 처음 코드 -> combinations를 사용해서 모든 조합을 다 계산 -> 불필요한 연산. 고로 시간 초과가 남.
# 아이디어: 각 종류에서 경우의 수는 (해당 종류의 의상 개수 + 1)이다 (!) -> 선택 안함이 포함됨.
from itertools import combinations
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  dt = dict()
  n = int(input().strip())
  
  for _ in range(n):
    name, case = input().strip().split()
    dt[case] = dt.get(case, 0) + 1 # 아래보다 좀 더 개선된 코드

  answer = 1
  for count in dt.values():
    answer *= (count + 1)
  print(answer - 1)