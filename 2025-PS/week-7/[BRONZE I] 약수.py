# https://www.acmicpc.net/problem/1037

# 내 답안
# 맞추고 나서 생각해보니 꼭 가운데 것들을 곱해야 하는 건 아닌 ... => max(numbers) * min(numbers) 해도 됨
count = int(input())
numbers = sorted(list(map(int, input().split())))
if count % 2 == 1:
  print(numbers[count//2] ** 2)
else:
  print(numbers[count//2 - 1] * numbers[count//2])