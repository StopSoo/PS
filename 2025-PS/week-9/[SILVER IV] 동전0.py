# https://www.acmicpc.net/problem/11047

# 내 답안
# 걸린 시간: 40ms
# 항상 예외 처리를 신경 쓸 것 !!
N, price = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
max_index = 0
for i in range(len(coins)-1):
  if price < coins[i+1]:
    max_index = i
    break
else: max_index = len(coins)-1 # 가장 큰 동전보다 큰 금액이라면 마지막 인덱스를 넣기

for coin in coins[:max_index+1][::-1]:
  if price == 0: break
  count += price // coin
  price = price % coin

print(count)