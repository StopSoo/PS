# https://www.acmicpc.net/problem/2470

# 내 답안
# 걸린 시간: 136ms
# 알고리즘: 이분탐색/투포인터
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = sorted(map(int, input().strip().split()))
# 투포인터
i, j = 0, N - 1
max_abs = float('inf')
answer = [0, 0]
while i < j:
  now = numbers[i] + numbers[j]
  if now > 0:
    if abs(now) < max_abs:
      max_abs = abs(now)
      answer = [numbers[i], numbers[j]]
    else: j -= 1
  elif now == 0:
    answer = [numbers[i], numbers[j]]
    break
  else:
    if abs(now) < max_abs:
      max_abs = abs(now)
      answer = [numbers[i], numbers[j]]
    else: i += 1

print(*answer)