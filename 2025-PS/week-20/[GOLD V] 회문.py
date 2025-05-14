# https://www.acmicpc.net/problem/17609

# 내 답안
# 걸린 시간: 524ms
# 알고리즘: 문자열 / 투포인터
# 투포인터로 유사회문 판별 방법: 양쪽 끝에서 투포인터 시작 -> 문자가 같으면 포인터 둘 다 이동, 다르면 두 문자 중 하나를 제거해 회문이 되는지 판단.
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  word = input().strip()
  
  if word == word[::-1]: print(0) # 회문일 경우
  else:
    left, right = 0, len(word) - 1
    while left < right:
      if word[left] == word[right]:
        left += 1
        right -= 1
      else:
        new_word1 = ''.join([word[i] for i in range(len(word)) if i != left])
        new_word2 = ''.join([word[i] for i in range(len(word)) if i != right])
        if new_word1 == new_word1[::-1] or new_word2 == new_word2[::-1]: print(1)
        else: print(2)
        break
