# https://www.acmicpc.net/problem/9084

# 내 답안
# 걸린 시간: 60ms
# 알고리즘: 배낭 문제 - 무한정 배낭 문제(동전은 무한정 쓸 수 있기 때문)
# 아이디어 1) 한 번에 하나의 동전 종류씩 고려해라.
# 아이디어 2) dp[i] = i원을 만드는 경우의 수 
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input()) # 동전 종류 수
  coins = list(map(int, input().split()))
  price = int(input()) # 만들어야 하는 금액

  dp = [0] * (price + 1)
  dp[0] = 1 # 0원을 만드는 경우의 수는 1
  for coin in coins: # 동전 순서대로 루프를 돌기 때문에, 중복 없이 구현 가능(!)
    for i in range(coin, price + 1):
      dp[i] += dp[i - coin] # i원을 만들기 위해 coin을 마지막에 한 번 더 쓰는 경우를 누적(!)

  print(dp[-1])