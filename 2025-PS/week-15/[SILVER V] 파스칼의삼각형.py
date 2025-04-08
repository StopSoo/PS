# https://www.acmicpc.net/problem/16395

# 내 답안
# 걸린 시간: 36ms
# 원리를 이해한다면 쉬운 문제 ... n-1Ck-1이다!
from math import factorial

n, k = map(int, input().split())
print(factorial(n-1) // (factorial(k-1) * factorial(n-k)))

# DP로 푼다면
# 걸린 시간: 36ms
n, k = map(int, input().split())
pascal = [[1], [1, 1]]
if n > 2:
  for i in range(2, n):
    temp = []
    for j in range(i+1):
      if j == 0 or j == i:
        temp.append(1)
      else:
        temp.append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal.append(temp)

print(pascal[n-1][k-1])