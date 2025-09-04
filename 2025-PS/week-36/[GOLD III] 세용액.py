# https://www.acmicpc.net/problem/2473

# 내 답안
# 걸린 시간: 시간 초과 (아무래도 ..)
# 알고리즘: 조합 이용 
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
numbers = list(map(int, input().strip().split()))
answer = []
score = float('inf')
for comb in combinations(numbers, 3):
  if abs(sum(comb)) < score:
    answer = sorted(list(comb))
    score = abs(sum(comb))

print(*answer)

# 알고리즘: 이분 탐색 / 투포인터 -> 정렬!!
# 걸린 시간: 144ms
# 아이디어: 세 원소 중 하나를 고정으로 해두고 나머지 두 개를 이분탐색(!)
# 골드 치고 그렇게 어려운 문제는 아니나, 로직 생각을 좀 해야 하는 문제 !!
import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(map(int, input().strip().split()))

best = float('inf')
best_set = []
for first in range(0, N - 2):
  i = first + 1
  j = N - 1
  
  while i < j:
    now = numbers[first] + numbers[i] + numbers[j]
    if abs(best) > abs(now):
      best = now
      best_set = [numbers[first], numbers[i], numbers[j]]
      if now == 0: # 조기 종료
        print(*best_set)
        sys.exit(0)
    # 현재 조합의 결과값에 따라 투포인터를 조절
    if now > 0: j -= 1
    elif now < 0: i += 1
    else: break
  
print(*best_set)