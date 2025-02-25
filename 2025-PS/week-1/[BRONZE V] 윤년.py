# https://www.acmicpc.net/problem/2753

# 내 답안
# 파이썬은 &&와 || 대신 and와 or 사용
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print("1")
else:
  print("0")