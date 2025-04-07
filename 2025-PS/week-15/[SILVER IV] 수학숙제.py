# https://www.acmicpc.net/problem/2870

# 내 답안
# 걸린 시간: 36ms
N = int(input())
numbers = []
for _ in range(N):
  word = input()
  temp = ''
  for w in word:
    if w.isdigit(): temp += w
    elif temp != '': 
      numbers.append(int(temp))
      temp = '' # 초기화
  if temp != '': numbers.append(int(temp))

numbers.sort()
print(*numbers, sep='\n')