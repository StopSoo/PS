# https://www.acmicpc.net/problem/17299

# 내 답안
# 걸린 시간: 시간 초과
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = [0] + list(map(int, input().strip().split()))
count = defaultdict(int)
for n in A[1:]: count[n] += 1 # 개수 세기

NGF = [0] * (N + 1)
for i in range(1, N + 1):
  for j in range(i + 1, N + 1):
    if count[A[i]] < count[A[j]] and A[i] != A[j]:
      NGF[i] = A[j]
      break
  else:
    NGF[i] = -1
print(*NGF[1:])

# 스택을 활용한 답안
# 걸린 시간: 1836ms
# 오래 막혔던 부분: 스택에 값을 넣지 말고 "인덱스"를 넣어라 !!!!!
# + 1 기반 인덱스 잘 체크할 것 !!
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = [0] + list(map(int, input().strip().split()))
count = defaultdict(int)
for n in A[1:]: count[n] += 1 # 개수 세기

stack = []
NGF = [-1] * (N + 1)
for i in range(1, N + 1):
  while stack and count[A[stack[-1]]] < count[A[i]]:
    NGF[stack.pop()] = A[i]
  stack.append(i)
print(*NGF[1:])