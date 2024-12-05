# set을 활용한 풀이 체크 (*)
a, b, c = map(int, input().split()) # 주사위 눈 세 개
dice = [a, b, c]
unique_values = set(dice)

if len(unique_values) == 1: # 주사위 눈이 모두 같을 경우
  reward = 10000 + a * 1000
elif len(unique_values) == 2: # 주사위 눈들 중 두 개가 같을 경우
  for num in unique_values:
    if dice.count(num) == 2:
      reward = 1000 + num * 100
else: # 주사위 눈이 모두 다른 경우
  reward = max(dice) * 100

print(reward)