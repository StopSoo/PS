# https://www.acmicpc.net/problem/1316

# 내 답안
N = int(input())
count = 0
for _ in range(N):
  word = input()
  prev = '' # 이전 단어 체크
  checks = set()

  for w in word:
    if w != prev:  # 연속된 문자가 아닐 때만 체크
      if w in checks:  # 그룹 단어 X
        break
      checks.add(w)
    prev = w
  else:
    count += 1
print(count)