# https://www.acmicpc.net/problem/2143

# 내 답안
# 걸린 시간: 492ms
# 알고리즘: 이분 탐색 / 누적합
# 처음에 살짝 감이 안 잡혔어서 지피티로 풀이 흐름 도움 받음.
import sys
input = sys.stdin.readline
from collections import Counter
# 입력
T = int(input().strip())
n = int(input().strip())
A = list(map(int, input().strip().split()))
m = int(input().strip())
B = list(map(int, input().strip().split()))
# 누적합 구하기
s_A, s_B = [0, A[0]], [0, B[0]] # 누적합
for i in range(1, n): s_A.append(s_A[-1] + A[i])
for i in range(1, m): s_B.append(s_B[-1] + B[i])
# 합 종류 구하기 
subA, subB = [], []
for i in range(1, n + 1):
  for j in range(i, n + 1):
    subA.append(s_A[j] - s_A[i-1])
for i in range(1, m + 1):
  for j in range(i, m + 1):
    subB.append(s_B[j] - s_B[i-1])
# Counter 사용해서 두 배열의 합이 T인 조합 찾아내기
c_A = Counter(subA)
answer = 0
for s in subB:
  target = T - s
  answer += c_A[target]
print(answer)
