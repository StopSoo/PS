# https://www.acmicpc.net/problem/10988

# 내 답안
# 걸린 시간: 40ms
word = input()
if word == word[::-1]: print(1)
else: print(0)