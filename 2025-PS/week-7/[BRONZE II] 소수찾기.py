# https://www.acmicpc.net/problem/1978

# 내 답안
N = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
  flag = True
  if num == 1: continue
  for i in range(2, num):
    if num % i == 0:
      flag = False
      break
  if flag: count += 1
print(count)

# 약수 점검할 때 내가 짠 코드처럼 점검하기보다는, 시간 복잡도를 줄이기 위해 루트N까지만 점검하는 것이 좋을 듯 (!)