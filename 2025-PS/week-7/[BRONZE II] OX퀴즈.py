# https://www.acmicpc.net/problem/8958

# 내 답안
T = int(input())

for i in range(T):
  answers = input()
  final_point = 0
  current_point = 1

  for ans in answers:
    if ans == 'O':
      final_point += current_point
      current_point += 1
    else:
      current_point = 1 # 초기화
  print(final_point)