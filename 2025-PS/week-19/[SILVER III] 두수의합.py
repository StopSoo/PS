# https://www.acmicpc.net/problem/3273

# 내 답안
# 걸린 시간: 84ms
# 알고리즘: 투포인터
import sys
input = sys.stdin.readline

N = int(input())
l = sorted(map(int, input().split()))
x = int(input()) # 합

s, e = 0, N-1
count = 0
while s < e:
  if l[s] + l[e] == x:
    count += 1
    s += 1
    e -= 1 # 두 포인터 모두 이동시키기
  elif l[s] + l[e] > x: e -= 1
  else: s += 1

print(count)