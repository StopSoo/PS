# https://www.acmicpc.net/problem/15961

# 내 답안
# 걸린 시간: 3812ms
# 알고리즘: 슬라이딩윈도우
# 투포인터를 사용하더라도 윈도우 크기가 고정되어 있기 때문에 비슷한 로직이 됨!
import sys
input = sys.stdin.readline 
from collections import defaultdict

N, d, k, c = map(int, input().strip().split())
sushi = [int(input().strip()) for _ in range(N)]
sushi += sushi[:k-1] # for 슬라이딩윈도우

counter = defaultdict(int)
unique = 0 # 종류 수
for i in range(k):
  if counter[sushi[i]] == 0: unique += 1
  counter[sushi[i]] += 1
max_count = unique + (1 if counter[c] == 0 else 0) # 쿠폰 초밥 포함 여부 체크
# 슬라이딩 윈도우
for i in range(1, N):
  left = sushi[i - 1]
  counter[left] -= 1
  if counter[left] == 0: unique -= 1

  right = sushi[i + k - 1]
  if counter[right] == 0: unique += 1
  counter[right] += 1

  current_count = unique + (1 if counter[c] == 0 else 0) # 쿠폰 초밥 포함 여부 체크
  max_count = max(max_count, current_count)

print(max_count)
