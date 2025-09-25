# https://www.acmicpc.net/problem/10025

# 내 답안
# 걸린 시간:
# 알고리즘: 투포인터 / 슬라이딩윈도우
import sys 
input = sys.stdin.readline

N, K = map(int, input().strip().split())
buckets = []
for _ in range(N):
  g, x = map(int, input().strip().split())
  buckets.append((x, g))
# 위치 기준으로 정렬
buckets.sort() 

l, total, answer = 0, 0, 0
for r in range(N):
  total += buckets[r][1]
  # 윈도우 범위가 2*K를 초과하면 크기를 줄여줌
  while buckets[r][0] - buckets[l][0] > 2 * K:
    total -= buckets[l][1]
    l += 1
  answer = max(answer, total)

print(answer)