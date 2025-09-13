# https://www.acmicpc.net/problem/2467

# 내 답안
# 걸린 시간: 116ms
# 알고리즘: 투포인터 / 이분탐새
import sys
input = sys.stdin.readline

N = int(input().strip())
liquids = list(map(int, input().strip().split()))
answer = [0, 0]
min_diff = float('inf')
i, j = 0, N - 1 # 투포인터
while i < j:
  total = liquids[i] + liquids[j]
  if abs(total) <= min_diff:
    min_diff = abs(total)
    answer = [liquids[i], liquids[j]]
  # 포인터 이동 조건 체크 (!)
  if total < 0: i += 1
  elif total > 0: j -= 1
  else: break

print(*answer)