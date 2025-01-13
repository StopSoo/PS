# 시간 초과 위험이 있는 문제
# 중복된 문자들의 순열 개수를 팩토리얼로 정리 가능 (!)
# brute force / back tracking 이용 가능
from itertools import permutations
import math

S = input() # 문자열
luckys = 0

for words in permutations(S):
  ok = True
  for i in range(len(words)-1):
    if (words[i] == words[i+1]): 
      ok = False
      break
  luckys += ok

for i in range(ord('a'), ord('z') + 1):
  luckys //= math.factorial(S.count(chr(i)))

print(luckys)