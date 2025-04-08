# https://www.acmicpc.net/problem/1755

# 내 답안
# 걸린 시간: 36ms
# 다른 사람들 답안 확인해보니 replace를 써서 str화 할 수도 있다는 점 ~~!
numbers = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
str_numbers = {}
M, N = map(int, input().split())
for num in range(M, N+1):
  answer = ''
  for s in str(num):
    answer += numbers[s] + ' '
  str_numbers[answer.strip()] = num
for i, (str_num, number) in enumerate(sorted(str_numbers.items())):
  if i != 0 and i % 10 == 0: print()
  print(number, end=' ')