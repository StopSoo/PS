# https://www.acmicpc.net/problem/10986

# 내 답안
# 걸린 시간: 700ms
# 알고리즘: 누적합
# 아이디어: 이중 for문을 돌면 무조건 시간 초과
# 그래서 나머지를 따로 구해놓고 나머지가 같은 쌍들을 구한다 (!)
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().strip().split())
A = [0] + list(map(int, input().strip().split())) # 1 기반 인덱스

S = A[:]
mods = defaultdict(int) # 나머지가 같은 것들끼리 카운트
for i in range(1, N + 1): 
  S[i] += S[i-1]
  mods[S[i] % M] += 1

count = mods[0] # 그 자체로 나머지가 0인 것들 더해놓기
for mod in mods: # 나머지가 같은 것들끼리 쌍의 개수를 구해 더해주기
  val = mods[mod]
  count += (val * (val - 1) // 2)

print(count)