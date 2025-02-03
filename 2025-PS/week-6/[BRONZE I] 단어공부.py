# https://www.acmicpc.net/problem/1157

# 내 답안
word = input()
counts = [0] * 26
for w in word.upper(): counts[ord(w)-65] += 1
if counts.count(max(counts)) > 1: print('?')
else: print(chr(counts.index(max(counts)) + 65))