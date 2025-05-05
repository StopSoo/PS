# https://www.acmicpc.net/problem/9324

# 내 답안
# 걸린 시간: 564ms
# 처음에 시간초과 난 이유: answer 문자열을 따로 만들면서 진행해서.
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  word = input().strip()
  dt = dict()
  i = 0
  while i < len(word):
    dt[word[i]] = dt.get(word[i], 0) + 1
    if dt[word[i]] == 3:
      dt[word[i]] = 0 # 개수 초기화
      if i+1 < len(word) and word[i+1] == word[i]:
        i += 2
        continue 
      else: break
    i += 1
  else:
    print("OK")
    continue
  print("FAKE")