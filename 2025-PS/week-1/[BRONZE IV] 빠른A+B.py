import sys
# 빠른 입출력을 위해 sys.stdin.readline()을 사용
# rstrip(): 맨 끝 개행문자를 제거
T = int(sys.stdin.readline().rstrip())

for i in range(T):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  print(a + b)