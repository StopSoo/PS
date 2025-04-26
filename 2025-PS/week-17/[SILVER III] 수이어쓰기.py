# https://www.acmicpc.net/problem/1515

# 내 답안
# 틀린 답안 -> 일단 인덱싱하는 과정이 너무 복잡하고 분기가 너무 나뉨
numbers = input()
s = 1 # 시작 숫자
i = 0 # 인덱스
while i < len(numbers):
  if int(numbers[i:i+len(str(s))]) == s:
    if i < len(numbers)-1: s += 1 # 비교 숫자 증가
    i += len(str(s)) # 인덱스 증가
  else:
    while True:
      if numbers[i] not in str(s):
        s += 1
      else:
        common = 1
        while common <= len(str(s)):
          if numbers[i:i+common] in str(s): common += 1
          else: 
            i += common-1
            break
        if i < len(numbers)-1: s += 1
        break

print(s)

# 정답
# 걸린 시간: 60ms
numbers = input().strip()
n = 1
j = 0  # numbers에서 비교할 인덱스

while True:
  for c in str(n):
    if j < len(numbers) and c == numbers[j]:
      j += 1
  if j == len(numbers):
    print(n)
    break
  n += 1