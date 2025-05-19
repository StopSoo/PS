# https://www.acmicpc.net/problem/1544

# 내 답안
# 걸린 시간: 36ms
import sys
input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
  word = input().strip()
  if not word_list: word_list.append(word)
  else:
    for i in range(len(word)):
      temp = word[i:] + word[:i]
      if temp in word_list: break
    else: word_list.append(word)

print(len(word_list))