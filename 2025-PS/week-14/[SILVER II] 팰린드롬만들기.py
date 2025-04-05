# https://www.acmicpc.net/problem/1254

# 내 답안
# 걸린 시간: 40ms
# 문제를 제대로 읽자 !! * 문자를 문자열 뒤에 추가해서 *
def check_p(word):
  if word == word[::-1]: return True
  else: return False

import sys
input = sys.stdin.readline

word = input().strip()
max_sw = '' # 팰린드롬 길이가 최대여야 함
answer = ''
if check_p(word): print(len(word)) # 주어진 문자가 팰린드롬이라면
else:
  # 부분 문자열들 구하기
  separate_words = [word[s:] for s in range(len(word))]
  for i, sw in enumerate(separate_words):
    if check_p(sw): # 팰린드롬이라면
      if len(max_sw) < len(sw): # 가장 긴 팰린드롬 찾기
        max_sw = sw
        answer = word[:i] + sw + word[:i]
  print(len(answer))