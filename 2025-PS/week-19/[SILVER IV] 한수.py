# https://www.acmicpc.net/problem/1065

# 내 답안
# 걸린 시간: 36ms
N = int(input())
count = 0
for number in range(1, N+1):
  number = str(number)
  if len(number) <= 2: # 두자리수까지는 모두 등차수열을 이룸
    count += 1
    continue
  gap = int(number[0]) - int(number[1])
  for i in range(1, len(number)-1):
    if int(number[i]) - int(number[i+1]) != gap: break
  else: count += 1
print(count)