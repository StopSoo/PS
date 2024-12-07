# 파일의 끝: EOFError
while 1:
  try:
    a, b = map(int, input().split())
    print(a + b)
  except EOFError:
    break