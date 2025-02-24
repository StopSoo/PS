# https://www.acmicpc.net/problem/1654

# 내 답안
# 걸린 시간: 60ms
import sys
input = sys.stdin.readline

K, N = map(int, input().strip().split())
lines = [int(input().strip()) for _ in range(K)]

# 이진 탐색 사용하기
answer = 0
left, right = 1, max(lines)
while left <= right: # 일반적인 이진탐색 조건
  mid = int(left/2 + right/2) # 숫자 범위가 크기 때문에 분배법칙을 사용
  count = sum([l // mid for l in lines])
  if count >= N : # N보다 커도 N개라고 인정됨
    answer = mid # 최대 길이 갱신
    left = mid + 1 # 더 긴 랜선도 가능한지 확인
  elif count < N:
    right = mid - 1

print(answer)