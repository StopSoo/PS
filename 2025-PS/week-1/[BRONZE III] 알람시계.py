# https://www.acmicpc.net/problem/2884

# 내 답안
# 빠진 경우의 수가 있진 않은지 잘 체크할 것
H, M = map(int, input().split())

if M < 45:
  H = (H + 23) % 24
M = (M + 15) % 60

print(H, M)