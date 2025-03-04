# https://www.acmicpc.net/problem/11005

# 내 답안
# 걸린 시간: 40ms
import sys
input = sys.stdin.readline

N, B = map(int, input().strip().split())
result = ''
while True:
  if N % B < 10:
    result += str(N%B)
  else:
    result += chr(N % B + 55)
  N = N // B
  if N == 0: break
print(result[::-1])