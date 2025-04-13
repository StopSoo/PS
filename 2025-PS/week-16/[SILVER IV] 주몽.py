# https://www.acmicpc.net/problem/1940

# 내 답안
# 걸린 시간: 44ms
# 이 문제를 보고 정렬+투포인터를 사용하면 좋다는 것을 떠올릴 수 있도록 (!)
# 조합을 사용해서 푼다면 시간 초과가 난다.
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
numbers = sorted(map(int, input().strip().split())) # 정렬 먼저 하기

left, right = 0, N-1
answer = 0
while left < right:
  s = numbers[left] + numbers[right]
  if s == M: 
    answer += 1
    left += 1
    right -= 1
  elif s < M: left += 1
  elif s > M: right -= 1
print(answer)