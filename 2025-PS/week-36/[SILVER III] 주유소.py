# https://www.acmicpc.net/problem/13305

# 내 답안
# 걸린 시간: 100ms
# 알고리즘: 그리디 

# 핵심 아이디어 !!!!!!
# 1. 왼쪽 도시부터 차례로 이동.
# 2. 지금까지 본 가장 싼 주유소 가격으로 다음 도시까지 이동할 기름을 사면 됨.
# 3. 다음 도시에서 가격이 더 싸면 갱신.
import sys
input = sys.stdin.readline

N = int(input().strip()) # 도시의 개수
roads = list(map(int, input().strip().split())) # 도로 길이 (N-1개)
prices = list(map(int, input().strip().split())) # 주유소 가격 (N개)

total_cost = 0
min_price = prices[0] # 최소 비용을 유지

for i in range(N - 1):  # 마지막 도시 전까지만 순회
  if prices[i] < min_price: # 갱신할 필요가 있을 때만 갱신
    min_price = prices[i]
  total_cost += min_price * roads[i]

print(total_cost)