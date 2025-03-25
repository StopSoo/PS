# https://www.acmicpc.net/problem/10610

# 내 답안
# 걸린 시간: 48ms
# 30의 배수 -> 일단 0으로 끝나야 함 / 3의 배수여야 함(= 자릿수들의 합이 3의 배수여야 함)
str_number = input()

if '0' not in str_number: 
  print(-1)
else:
  if sum(map(int, str_number)) % 3 != 0:
    print(-1)
  else:
    print(''.join(sorted(str_number, reverse=True)))