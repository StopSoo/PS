# https://www.acmicpc.net/problem/16139

# 내 답안
# 걸린 시간: 56ms / 50점
import sys
input = sys.stdin.readline
print = sys.stdout.write

word = input().strip()
q = int(input().strip())
dt = dict()
for i in range(0, 26): # 딕셔너리 초기화
  dt[chr(i+97)] = [-1] * len(word)

for _ in range(q):
  alpha, l, r = input().strip().split()
  # 한 번 dp한 alpha가 아니라면
  if dt[alpha] == [-1] * len(word):
    if word[0] == alpha: dt[alpha][0] = 1 # 첫 글자 초기화
    else: dt[alpha][0] = 0
    for i in range(1, len(word)):
      dt[alpha][i] = dt[alpha][i-1] + (1 if word[i] == alpha else 0)
  
  if int(l) != 0: print(str(dt[alpha][int(r)] - dt[alpha][int(l)-1]) + '\n')
  else: print(str(dt[alpha][int(r)]) + '\n')