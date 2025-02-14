# https://www.acmicpc.net/problem/10250

# 내 답안
# 반례를 찾아서 꼭 체크해보기!
T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  if N % H == 0:
    floor, number = H, N // H
    print(floor * 100 + number)
  else:
    floor, number = N % H, N // H + 1
    print(floor * 100 + number)