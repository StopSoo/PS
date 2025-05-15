# https://www.acmicpc.net/problem/8892

# 내 답안
# 걸린 시간: 144ms
import sys
input = sys.stdin.readline
from itertools import combinations

T = int(input())
for _ in range(T):
  N = int(input())
  words = [input().strip() for _ in range(N)]
  for comb in combinations(words, 2):
    new_word1 = comb[0] + comb[1]
    new_word2 = comb[1] + comb[0]
    if new_word1 == new_word1[::-1]:
      print(new_word1)
      break
    if new_word2 == new_word2[::-1]:
      print(new_word2)
      break
  else: print(0)