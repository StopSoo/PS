# https://www.acmicpc.net/problem/2869

# 내 답안
A, B, V = map(int, input().split())
answer = 1 # 날짜 수
height = 0
while height != V:
  height += A
  if height >= V: break
  height -= B
  if height >= V: break
  answer += 1
print(answer)