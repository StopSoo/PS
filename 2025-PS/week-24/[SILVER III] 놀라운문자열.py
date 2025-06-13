# https://www.acmicpc.net/problem/1972

# 내 답안
# 걸린 시간: 36ms
# 자료구조: 문자열
# 나는 리스트를 사용했지만 딕셔너리를 사용할 수도 있다는 것 알아두기! (조회할 때 시간 복잡도가 낮으므로)
import sys
input = sys.stdin.readline

while True:
  word = input().strip()
  if word == '*': break
  
  flag = True
  len_word = len(word)
  for gap in range(1, len_word):
    l = []
    for i in range(0, len_word - gap):
      new_word = word[i:i+gap+1:gap]
      if new_word in l:
        flag = False           
        break
      else: l.append(new_word)
    if not flag:
      print(word, "is NOT surprising.")
      break  
  else: print(word, "is surprising.")
