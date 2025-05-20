# https://www.acmicpc.net/problem/6443

# 첫 번째 답안: 내장 모듈 사용하기
# 시간 초과 ~ 
# from itertools import permutations # 순열
# import sys
# input = sys.stdin.readline

# N = int(input())
# for _ in range(N):
#   s = set()
#   word = input().strip()
#   for p in permutations(word, len(word)):
#     s.add(''.join(p))
#   print('\n'.join(sorted(s)))

# 두 번째 답안: 백트래킹
# 걸린 시간: 400ms
# 중복된 문자를 고려해주지 않으면 시간 초과가 남.
# 아이디어) 입력으로 받는 문자를 정렬한 후, 같은 단어일 때는 고려하지 않도록 할 것(!)
# 그걸 어떻게 하냐? prev에 해당 depth에서 사용했던 문자를 저장. 겹치지 않도록 그 depth에 다른 문자 사용.
# 또한 0부터 시작해서 depth == len(word)인지 비교하는 것도 기본이니까 잊지 말 것.
# 대충 알고 휘갈기지 말고, 제대로 알자!
import sys
input = sys.stdin.readline

def back(depth):
  global ans, checked
  
  if depth == len(word):
    print(''.join(ans))
    return
  
  prev = '' # 이번 depth에서 사용한 문자 기록
  for i in range(len(word)):
    if not checked[i] and word[i] != prev:
      ans.append(word[i])
      checked[i] = 1
      back(depth + 1)
      checked[i] = 0
      ans.pop()
      prev = word[i] # 지금 문자를 이전 문자로 업데이트

N = int(input())
for _ in range(N):
  word = sorted(input().strip()) # 정렬해서 같은 문자끼리 붙도록.
  ans = []
  checked = [0] * len(word)
  back(0)