# https://www.acmicpc.net/problem/4796

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 그리디 
# 처음에 문제를 이해하는 데 좀 시간이 걸림.
import sys
input = sys.stdin.readline

i = 1 # 인덱스 
while True:
  L, P, V = map(int, input().strip().split())
  if L == P == V == 0: 
    break
  day = (V // P) * L + min(V % P, L)
  print("Case " + str(i) + ": " + str(day))
  i += 1