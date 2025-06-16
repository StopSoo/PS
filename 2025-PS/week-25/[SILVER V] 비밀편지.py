# https://www.acmicpc.net/problem/5426

# 내 답안
# 걸린 시간: 80ms
T = int(input())
for i in range(T):
  message = list(input().strip())
  width = int(len(message) ** 0.5)
  rotated_message = [message[(width - i - 1) + width * j] for i in range(width) for j in range(width)]
  print(''.join(rotated_message))