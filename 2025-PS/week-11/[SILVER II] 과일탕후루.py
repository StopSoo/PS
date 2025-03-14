# https://www.acmicpc.net/problem/30804

# 답안
# 걸린 시간: 224ms
# 투포인터 알고리즘 (!) 
import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

left, right = 0, 0
answer = 0 # 제출할 정답
fruit_count = {}

while right < N: # O(N)의 시간 복잡도
  # 딕셔너리에 값 추가
  fruit_count[l[right]] = fruit_count.get(l[right], 0) + 1

  while len(fruit_count) > 2:
    fruit_count[l[left]] -= 1 # 유효한 구간을 유지
    if fruit_count[l[left]] == 0:
      del fruit_count[l[left]]
    left += 1
  
  answer = max(answer, right - left + 1) # 최댓값 갱신
  right += 1

print(answer)