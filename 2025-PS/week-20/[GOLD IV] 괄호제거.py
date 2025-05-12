# https://www.acmicpc.net/problem/2800

# 내 답안
# 걸린 시간: 36ms
# 주의할 점 1) 괄호 짝 지을 때 처음에 했던 것처럼 right는 역순으로만 배치하는 것은 틀린 풀이 (!) -> 스택을 사용해서 할 것.
# 주의할 점 2) 답변 저장할 때 집합에 저장해서 중복 제거할 것 (!)
from itertools import combinations

word = input()
# 괄호 짝을 찾아 인덱스 저장해놓기
stack = []
couples = []
for i, ch in enumerate(word):
  if ch == '(': stack.append(i)
  elif ch == ')': 
    start = stack.pop()
    couples.append((start, i))

answers = set()
for i in range(1, len(couples)+1): # 공집합을 제외한 부분집합 찾기
  for comb in combinations(couples, i):
    list_word = list(word)
    for s, e in comb: 
      list_word[s] = ''
      list_word[e] = ''
    answers.add(''.join(list_word))

for ans in sorted(answers):
  print(ans)