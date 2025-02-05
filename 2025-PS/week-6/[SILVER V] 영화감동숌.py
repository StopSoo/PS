# https://www.acmicpc.net/problem/1436

# 내 답안
count = 0
number = 666

N = int(input())
while True:
  if "666" in str(number):
    count += 1
    if count == N:
      print(number)
      break
  number += 1