# https://www.acmicpc.net/problem/15312

# 내 답안
# 걸린 시간: 1428ms
he = input()
she = input()
numbers = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

values = []
for i in range(len(he)):
  values.append(numbers[ord(he[i]) - 65])
  values.append(numbers[ord(she[i]) - 65])

while len(values) != 2:
  temp = []
  for i in range(len(values)-1):
    temp.append((values[i] + values[i+1]) % 10)
  values = temp[:]
print(str(values[0]) + str(values[1]))
