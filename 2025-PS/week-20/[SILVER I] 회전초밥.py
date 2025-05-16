# https://www.acmicpc.net/problem/2531

# 내 답안
# 걸린 시간: 3340ms
# 슬라이딩윈도우로 풀려고 했지만, 살리지 못함
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().strip().split())
sushi = [int(input().strip()) for _ in range(N)]
sushi += sushi[:k-1]

max_count = 0
for s in range(N):
  now = sushi[s:s+k][:]
  if len(set(now)) >= max_count:
    max_count = len(set(now))
    if c not in now: max_count += 1

print(max_count)

# 슬라이딩 윈도우로 풀이한 코드
# 걸린 시간: 96ms (!)
import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input().strip()) for _ in range(N)]
sushi += sushi[:k-1]

counter = defaultdict(int)
unique = 0
# 초기 윈도우 세팅
for i in range(k):
  if counter[sushi[i]] == 0:
    unique += 1
  counter[sushi[i]] += 1
# 쿠폰 초밥 포함 여부 확인
max_count = unique + (1 if counter[c] == 0 else 0)
# 슬라이딩 윈도우
for i in range(1, N):
  # 윈도우에서 나가는 초밥
  left = sushi[i - 1]
  counter[left] -= 1
  if counter[left] == 0:
    unique -= 1
  # 윈도우에 새로 들어오는 초밥
  right = sushi[i + k - 1]
  if counter[right] == 0:
    unique += 1
  counter[right] += 1
  # 쿠폰 초밥 추가 여부 확인
  current_count = unique + (1 if counter[c] == 0 else 0)
  max_count = max(max_count, current_count)

print(max_count)
