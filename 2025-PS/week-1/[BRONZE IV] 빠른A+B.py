# https://www.acmicpc.net/problem/15552

# 내 답안
# 빠른 입출력을 위해 sys.stdin.readline()을 사용
# rstrip(): 맨 끝 개행문자를 제거
import sys
input = sys.stdin.readline
T = int(input().rstrip())

for i in range(T):
  a, b = map(int, input().rstrip().split())
  print(a + b)