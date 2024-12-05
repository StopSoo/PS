H, M = map(int, input().split())
time = int(input())

if M + time < 60:
  M = M + time
else:
  h = (M + time) // 60

  H = (H + h) % 24
  M = (M + time) % 60

print(H, M)