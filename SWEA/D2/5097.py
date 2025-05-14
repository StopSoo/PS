# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTVjgHKbn8DFAVT&categoryId=AWTVjgHKbn8DFAVT&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

# 내 답안
# import sys
# input = sys.stdin.readline
from collections import deque

T = int(input())
for i in range(T):
  N, M = map(int, input().strip().split())
  deq = deque(list(map(int, input().strip().split())))
  deq.rotate(-M)
  print(f'#{i+1} {deq[0]}')