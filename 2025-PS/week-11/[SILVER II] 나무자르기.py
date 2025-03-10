# https://www.acmicpc.net/problem/2805

# 내 답안
# 걸린 시간: 944ms (pypy3)
# 이분 탐색 -> 변수 바운더리가 굉장히 넓으므로 ...!
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))

left = 0
right = sorted(heights)[-1]-1 # 최댓값-1부터 탐색 가능하다는 점 (!)
while True:
  if left > right:
    print(right) # 위 조건 시 right를 출력해야 정답이 나옴 (!)
    break

  mid = (left + right) // 2
  result = sum([height - mid for height in heights if height-mid > 0])
  if result > M: left = mid + 1
  elif result < M: right = mid - 1
  else: 
    print(mid)
    break

