# https://www.acmicpc.net/problem/10951

# 내 답안
# 파일의 끝: EOFError
while 1:
  try:
    a, b = map(int, input().split())
    print(a + b)
  except EOFError:
    break