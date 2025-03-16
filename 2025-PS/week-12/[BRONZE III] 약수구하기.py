# https://www.acmicpc.net/problem/2501

# 내 답안
# 걸린 시간: 36ms
N, K = map(int, input().split())
numbers = []
for i in range(1, N+1):
  if N % i == 0: numbers.append(i)
print(numbers[K-1] if len(numbers) >= K else 0)