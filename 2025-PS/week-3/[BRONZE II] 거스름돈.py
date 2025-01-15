# 그리디 알고리즘
price = int(input()) # 물건의 금액
change = 1000 - price
count = 0 # 거스름돈 개수

while (1):
  if (change == 0):
    break

  if (change >= 500):
    count += (change // 500)
    change %= 500
  elif (change >= 100):
    count += (change // 100)
    change %= 100
  elif (change >= 50):
    count += (change // 50)
    change %= 50
  elif (change >= 10):
    count += (change // 10)
    change %= 10
  elif (change >= 5):
    count += (change // 5)
    change %= 5
  else:
    count += change
    change %= 1

print(count)

# 동전 사용 가능 개수를 고려하는 방법 -> 모든 경우 고려
money = 1000 - int(input())

ans = int(1e8)

for c500 in range(2):
  for c100 in range(10):
    for c50 in range(20):
      for c10 in range(100):
        for c5 in range(200):
          value = (c500 * 500) + (c100 * 100) + (c50 * 50) + (c10 * 10) + (c5 * 5)
          if money - value >= 0:
            ans = min(ans, c500 + c100 + c50 + c10 + c5 + (money - value))

print(ans)