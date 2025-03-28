# https://www.acmicpc.net/problem/1213

# 내 답안
# 답안은 맞게 나오지만, 시간 초과 나는 코드 
from itertools import permutations

word = input()
answers = []
for perm in set(permutations(list(word), len(word))):
  if ''.join(perm) == ''.join(perm)[::-1]: answers.append(''.join(perm))

print(sorted(answers)[0] if answers else "I'm Sorry Hansoo")

# 내 두 번째 답안
# 걸린 시간: 36ms
# 나름 투포인터 ...? 기본적으로 그리디 알고리즘 적용!
import math

word = sorted(list(input()))
lw = len(word)
answers = [''] * len(word)

ch = 'A'
left, right = 0, len(word)-1
flag = True
while len(word) != 0:
  if ch in word:
    if word.count(ch) >= 2:
      answers[left] = answers[right] = ch
      left += 1
      right -= 1
      word = word[2:]
    else:
      if answers[math.ceil(lw/2)-1] == '': # 비어있을 경우에만 정가운데에 넣기
        answers[math.ceil(lw/2)-1] = ch 
        word = word[1:]
      else:
        flag = False
        break
  else:
    ch = chr(ord(ch) + 1) # 다음 문자로 넘어가기

if flag: print(''.join(answers))
else: print("I'm Sorry Hansoo")