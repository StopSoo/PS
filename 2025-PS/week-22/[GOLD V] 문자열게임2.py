# https://www.acmicpc.net/problem/20437

# 내 답안
# 걸린 시간: 324ms
# 알고리즘/자료구조: 문자열 / 슬라이딩윈도우
# 문제 이해를 완전히 하지는 못한 채로 풀어서 중간에 막혔음 ㅜㅜ 아래 코드를 보며 복습하면 될 듯!
import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
  W = input().strip()
  K = int(input())
  shortest = float('inf')
  longest = 0

  pos = defaultdict(list)
  for idx, ch in enumerate(W): pos[ch].append(idx) # 문자별 인덱스 수집

  for ch in pos:
    indices = pos[ch]
    if len(indices) < K: continue   
    # 해당 문자의 연속된 K개의 위치 중에서 최소 길이, 최대 길이 갱신
    for i in range(len(indices) - K + 1):
      start = indices[i]
      end = indices[i + K - 1]
      length = end - start + 1
      shortest = min(shortest, length)
      longest = max(longest, length)
  # 출력
  if shortest != float('inf'): print(shortest, longest)
  else: print(-1)


# 내가 처음에 짰던 코드
import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
  W = input().strip()
  K = int(input())
  shortest = float('inf')
  longest = 0
  for size in range(K, len(W)+1):
    dt = defaultdict(int)
    for i in range(0, size): dt[W[i]] += 1
    if any(val == K for val in dt.values()):
      shortest = min(shortest, K)
      if W[0] == W[K-1]: longest = max(longest, K)
    for i in range(1, len(W) - size + 1):
      dt[W[i-1]] -= 1
      dt[W[i + size - 1]] += 1
      if dt[W[i + size - 1]] == K:
        if shortest > size:
          shortest = size
        if W[i] == W[i + size - 1]: 
          longest = max(longest, size)
  # 출력
  if shortest != float('inf'): print(shortest, longest)
  else: print(-1)