# https://www.acmicpc.net/problem/27964

# 내 답안
# 걸린 시간: 48ms
import sys
input = sys.stdin.readline

N = int(input())
food_list = input().strip().split()
cheese_list = []
for food in food_list:
  if not food.endswith('Cheese'): continue
  elif food not in cheese_list: cheese_list.append(food)

print("yummy" if len(cheese_list) >= 4 else "sad")