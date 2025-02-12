# https://www.acmicpc.net/problem/10809

# 내 답안
# print(*리스트): 리스트 원소들을 공백을 가지고 한 줄로 출력
checks = [-1] * 26
word = input()
for i, w in enumerate(word):
  if (checks[ord(w)-97] == -1):
    checks[ord(w)-97] = i
print(*checks)