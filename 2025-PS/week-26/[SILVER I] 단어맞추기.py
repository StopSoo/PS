# https://www.acmicpc.net/problem/9081

# 내 답안
# 걸린 시간: 메모리 초과 (!!!)
import sys
input = sys.stdin.readline
from itertools import permutations    

T = int(input())
for _ in range(T):
  word = input().strip()
  word_list = sorted(set(list(permutations(word, len(word)))))
  size = len(word_list)

  idx = 0
  for i in range(size):
    if word_list[i] == list(word): 
      if i + 1 <= size - 1: idx = i + 1
      else: idx = i
  print(''.join(word_list[idx]))

# next_permutation 알고리즘을 활용한 답안
# 걸린 시간: 32ms
import sys
input = sys.stdin.readline

def next(word):
  # 왼쪽에 있는 수보다 오른쪽에 있는 수가 더 큰 경우에만 탐색
  for i in range(len(word) - 1, 0, -1):
    if word[i-1] < word[i]:
      # 오른쪽에서부터 i보다 큰 숫자인 경우를 찾음
      for j in range(len(word) - 1, i-1, -1):
        # 두 수를 swap하고 i부터 마지막까지 워소 뒤집기
        if word[i-1] < word[j]:
          word[i-1], word[j] = word[j], word[i-1]
          return word[:i] + word[i:][::-1]
  return word # 해당되지 않는 경우 그대로 출력

T = int(input())
for _ in range(T):
  word = list(input().strip())
  result = ''.join(next(word))
  print(result)