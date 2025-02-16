# https://www.acmicpc.net/problem/2798

# 내 답안
# 걸린 시간: 68ms
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for comb in combinations(cards, 3):
  if sum(comb) > answer and sum(comb) <= M: answer = sum(comb)
print(answer)