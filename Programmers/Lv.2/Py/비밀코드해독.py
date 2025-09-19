# https://school.programmers.co.kr/learn/courses/30/lessons/388352

# intersection or &
from itertools import combinations

def solution(n, q, ans):
  answer = 0
  for numbers in combinations(range(1, n + 1), 5): # 가능한 모든 조합 생성
    check = True
    for i, ex in enumerate(q):
      if len(set(ex).intersection(set(numbers))) != ans[i]:
        check = False
        break
    if check:
      answer += 1
  
  return answer