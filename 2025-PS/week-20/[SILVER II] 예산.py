# https://www.acmicpc.net/problem/2512

# 내 답안
# 걸린 시간:
# 알고리즘: 이분탐색
# 이분탐색을 너무 복잡하게 생각하는 경향이 있는 것 같음 (!)
import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().strip().split()))
max_budget = int(input())

left, right = 1, max(budgets) # left는 1부터 시작(!)
answer = 0
while left <= right:
  mid = (left + right) // 2
  val = sum(budget if budget <= mid else mid for budget in budgets)
  
  if max_budget < val: 
    right = mid - 1
  elif max_budget >= val: 
    answer = mid # 값 갱신
    left = mid + 1 # 후에도 계속 추적

print(answer)