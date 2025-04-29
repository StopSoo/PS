# https://www.acmicpc.net/problem/7795

# 내 답안
# 시간 초과 나는 코드 (!)
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  answer = 0
  n, m = map(int, input().strip().split())
  A = sorted(map(int, input().strip().split()))
  B = sorted(map(int, input().strip().split()))

  for i in range(n):
    if A[i] > B[-1]: 
      answer += m * (n - i)
      break
    for j in range(m):
      if A[i] <= B[j]:
        answer += j
        break
  print(answer)

# 투포인터 활용한 답안
# 걸린 시간: 148ms
# A, B 모두 정렬되어 있으므로 투포인터 알고리즘 사용 가능.
# 시간 복잡도는 O(n + m)
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  answer = 0
  n, m = map(int, input().strip().split())
  A = sorted(map(int, input().strip().split()))
  B = sorted(map(int, input().strip().split()))

  i, j = 0, 0
  while i < n and j < m:
    if A[i] > B[j]: j += 1
    else: 
      answer += j
      i += 1
  answer += (n-i) * m # 나머지 더해주기

  print(answer)
