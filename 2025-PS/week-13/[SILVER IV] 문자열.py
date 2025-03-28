# https://www.acmicpc.net/problem/1120

# 내 답안
# 걸린 시간: 60ms
# 처음에 경우를 잘못 나눠서 완전 복잡하게 코드를 짰더니 '틀렸습니다'가 나옴.
# 차라리 브루트포스로 생각을 해보니, 간단했음 !! 해결 !!
# 기본적으로는 BFS가 맞음.
from collections import deque

def count_gap(A, B):
  count = 0
  for a, b in zip(A, B):
    if a != b: count += 1
  return count

A, B = input().split()

gap = float('inf')
deq = deque([A])
while deq:
  word = deq.popleft()
  if len(word) == len(B):
    gap = min(gap, count_gap(word, B))
  elif len(word) > len(B): break
  else:
    if word in B:
      gap = 0
      break
    else:
      for i in range(0, len(B) - len(word)+1): # 슬라이딩 윈도우 개념 사용
        gap = min(gap, count_gap(B[:i]+word+B[i+len(word):], B))

print(gap)