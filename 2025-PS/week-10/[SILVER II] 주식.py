# https://www.acmicpc.net/problem/11501

# 답안
# 풀이 방법
# 1. 더 미래의 날짜부터 거꾸로 주식의 가격을 탐색한다.
# 2. 앞에서부터 탐색한다면 미래에 어떤 가격이 있을지 모르기 때문이다.
# 3. 현재의 주식 가격이 현재 기록되어 있는 최대 가격보다 작다면 차익을 실현한다. 그렇지 않다면 현재 최대 가격 기록을 현재의 가격으로 갱신한다.
T = int(input())

for t in range(T):

  N = int(input())
  price = list(map(int, input().split()))

  money = 0 # 이익

  maxPrice = 0 # 주식의 최대 가격
  for i in range(len(price)-1, -1, -1):
    if price[i] > maxPrice:
      maxPrice = price[i]
    else: # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
      money += maxPrice - price[i]

  print(money)