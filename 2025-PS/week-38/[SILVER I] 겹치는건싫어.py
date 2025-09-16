# https://www.acmicpc.net/problem/20922

# 내 답안
# 걸린 시간: 320ms
# 알고리즘: 투포인터
import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

dt = defaultdict(int)
max_len = 0
i, j = 0, 1
dt[a[0]] += 1
while i <= j < N:
  if dt[a[j]] + 1 <= K:
    dt[a[j]] += 1
    j += 1
  else:
    max_len = max(max_len, j - i)
    dt[a[i]] -= 1
    i += 1

max_len = max(max_len, j - i) # 디버깅 시 놓치고 있던 부분 (!)
print(max_len)

# 지피티가 알려준 정석 스타일 코드
# 알고리즘: 투포인터
# 걸린 시간" 276ms
import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))

dt = defaultdict(int)
max_len = 0
i = 0

for j in range(N):
  dt[a[j]] += 1
  # 조건 위반 시 왼쪽 포인터 이동
  while dt[a[j]] > K:
    dt[a[i]] -= 1
    i += 1
  
  max_len = max(max_len, j - i + 1) # 매 반복마다 갱신

print(max_len)
