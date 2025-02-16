# https://www.acmicpc.net/problem/11050

# 내 답안
# 걸린 시간: 36ms
from math import factorial
N, K = map(int, input().split())
print(factorial(N) // (factorial(K) * factorial(N-K)))