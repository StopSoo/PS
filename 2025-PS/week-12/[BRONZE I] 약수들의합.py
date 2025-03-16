# https://www.acmicpc.net/problem/9506

# 내 답안
# 걸린 시간: 64ms
while True:
  N = int(input())
  if N == -1: break

  numbers = []
  for i in range(1, N+1):
    if N % i == 0: numbers.append(i)
  if sum(numbers[:len(numbers)-1]) == N:
    print(N, "=", end=' ')
    print(' + '.join(map(str, numbers[:len(numbers)-1])))
  else:
    print(N, "is NOT perfect.")