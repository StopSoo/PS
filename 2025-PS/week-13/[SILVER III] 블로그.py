# https://www.acmicpc.net/problem/21921

# 내 답안
# 걸린 시간: 140ms
# 비교 기준 변수들을 초기화할 때 잘 생각하고 할 것 !!
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
days = list(map(int, input().split()))

answer = sum(days[:X])
s = sum(days[:X])
count = 1
for i in range(N-X):
  s = s - days[i] + days[i+X]
  if answer < s: 
    answer = s
    count = 1
  elif answer == s:
    count += 1

print(answer if answer else "SAD")
if answer: print(count)