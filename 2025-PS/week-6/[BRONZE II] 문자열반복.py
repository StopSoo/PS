# https://www.acmicpc.net/problem/2675

# 내 답안
T = int(input())
words = []
for i in range(T):
  str_count, word = input().split()
  words += [''.join([w * int(str_count) for w in word])]
for i in range(len(words)): print(words[i])