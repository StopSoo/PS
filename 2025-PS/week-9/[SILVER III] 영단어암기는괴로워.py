# https://www.acmicpc.net/problem/20920

# 답안 1 -> 시간 초과
import sys
input = sys.stdin.readline

answers = []
N, M = map(int, input().strip().split())
words = [input().strip() for _ in range(N)]
words = sorted(words, key=lambda x:[-(words.count(x)), -(len(x)), x])

i = 0
while True:
  if i == len(words): break
  if len(words[i]) >= M: 
    answers.append(words[i])
    i += words.count(words[i])
  else:
    i += 1
print(*answers, sep='\n')

# 답안 2 
# 걸린 시간: 344ms
# 풀이 포인트 1) 딕셔너리에 값 추가 시 이미 키가 존재할 경우, 존재하지 않을 경우를 구분하기 위해 -> dt.get(키, 기본값)을 사용.
# 풀이 포인트 2) lambda 함수 내 정렬 기준을 정할 때 내림차순으로 되길 원한다면 - 붙이기 (!)
import sys
input = sys.stdin.readline

answer = []
N, M = map(int, input().strip().split())
dt = dict()
for _ in range(N):
  word = input().strip()
  dt[word] = dt.get(word, 0) + 1 # 이 방법 기억하기 (!)
dt = sorted(dt, key=lambda x:[-dt[x], -len(x), x])
for word in dt:
  if len(word) >= M: print(word)

# 다른 사람의 코드 -> 복습 시 활용할 것
from sys import stdin
from collections import Counter

input = stdin.read().splitlines()

NM, *words = input
N, M = NM.split()

new_words = []
for word in Counter(words).most_common():
  if len(word[0]) >= int(M):
    new_words.append(word)

new_words.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

print("\n".join([word for word, _ in new_words]))